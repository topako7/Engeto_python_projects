"""
projekt3_election_scraper.py: třetí projekt do Engeto Online Akademie - Datový analytik s Pythonem
author: Tomáš Pakosta
email: tpakosta@gmail.com
discord: Tom P. (tom.pa.costa) Tom#2303
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv
import os

def main():
    # Check if the correct number of arguments are provided (script name + 2 arguments)
    if len(sys.argv) != 3:
        print("Usage: python project3_election_scraper.py <param1 - link to any district from https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ> <param2 - filename.csv>")
        sys.exit(1)

    # Retrieve the two parameters from the command-line arguments
    #url = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3205" #input parameter 1
    #election_data = "election_data.csv" #input parameter 2
        
    url = sys.argv[1]               # The URL of the district page (passed as the first argument)
    election_data = sys.argv[2]     # The name of the CSV file (passed as the second argument)

    # Call scrape_district to get district codes, locations, and links
    codes, locations, links = scrape_district(url)
    # Call scrape_municipality to get election data for each district
    registered, envelopes, valid, votes_results, file_header = scrape_municipality(links)

    # Prepare the header of the CSV file
    file_header = list(["code", "location", "registered", "envelopes", "valid"] + file_header)
    # Create a new CSV file with the appropriate header
    data_file = create_file(election_data, file_header)

    # Combine the results into a list
    election_results = [codes, locations, registered, envelopes, valid, votes_results]
    
    # Write the results to the CSV file
    write_result(data_file, file_header, election_results)

"""
def find_base_url(url, url2):
    parts = 0
    response = 0
    url_parts = url.split("/")
    url_parts = ['/' if item == '' else item for item in url_parts]
    base_url = url_parts[0]
    
    while response != 200:
        parts += 1
        base_url = base_url + "/" + url_parts[parts]
        print(base_url+url2)
        response = requests.get(base_url+url2)
        response = response.status_code

    print(base_url)
    return base_url
"""
    
def scrape_district(url):
    """
    Scrape election district data from the provided URL.

    Args: url (str): The URL of the district page to scrape.
    Returns: tuple: A tuple containing lists of district codes, locations, and links to municipality pages.
    """

    base_url = "https://www.volby.cz/pls/ps2017nss/"                                            # Set the base URL for the election site
    codes = list()                                                                              # Initialize an empty list to store district codes
    locations = list()                                                                          # Initialize an empty list to store location names
    links = list()                                                                              # Initialize an empty list to store links to the district pages

    html_text = requests.get(url)                                                   # load the html code
    soup_district = BeautifulSoup(html_text.text, 'html.parser')                              # html code + parser type
    #print(soup.prettify())
    main_div = soup_district.find("div", {"id": "inner"})       # find the main part of the text to analyze
    td_tags = main_div.find_all("td", {"class": "cislo"})               # find td tags with class="cislo"
    td_locations = main_div.find_all("td", {"class": "overflow_name"})  # find td tags with class of the location name
    
    #base_url = find_base_url(url, td_tags[0].find("a").get('href'))

    for td in td_tags:  
        a_tags = td.find("a")
        links.append(base_url + a_tags['href'])                                                 # save the link to the detail of votes
        codes.append(a_tags.text.strip())                                                       # save the code of the location

    for td in td_locations:
        locations.append(td.text.strip())                                                       # save the name of the location
    
    return codes, locations, links


def scrape_municipality(urls):
    """
    Scrape municipality election results from a list of URLs.

    Args: urls (list): A list of URLs for each municipality to scrape.
    Returns:  tuple: A tuple containing lists of registered voters, envelopes, valid votes, 
               election results per party, and CSV header fields.
    """


    file_header = []            # Initialize an empty list to store the header of the CSV file
    registered = []             # Initialize an empty list to store the number of registered voters
    envelopes = []              # Initialize an empty list to store the number of envelopes sent
    valid = []                  # Initialize an empty list to store the number of valid votes
    votes_results = []          # Initialize an empty list to store the vote results for each party

    for link in urls:
        text = requests.get(link)
        soup_municipality = BeautifulSoup(text.text, 'html.parser') 
        main_table = soup_municipality.find("table", {"id":"ps311_t1", "class": "table"})
        td_tags = main_table.find_all("td", {"class": "cislo", "data-rel":"L1"})
        registered.append(int(td_tags[0].get_text(strip=True).replace('\xa0','')))      #registered number
        envelopes.append(int(td_tags[2].get_text(strip=True).replace('\xa0','')))       #envelopes number
        valid.append(int(td_tags[3].get_text(strip=True).replace('\xa0','')))           #valid number

        div_votes = soup_municipality.find("div", {"id": "inner"})   # Find the main content of the page
        
        td_party_name = div_votes.find_all("td", {"class": "overflow_name", "headers":"t1sa1 t1sb2"}) # Find all the table data cells containing party names
        
        file_header = list(set(file_header + [td.get_text(strip=True) for td in td_party_name if td.get_text(strip=True)])) # Add the party names to the file header (removes duplicates)
        
        td_party_votes = div_votes.find_all("td", {"class": "cislo", "headers":"t1sa2 t1sb3"}) # Find all the table data cells containing party vote counts
        
        # Create a dictionary to store the votes for each party
        votes = {}
        for name, result in zip(td_party_name, td_party_votes):
            votes[name.text.strip()] = int(result.text.strip())
        
        votes_results.append(votes)
    return registered, envelopes, valid, votes_results, file_header


def create_file(name, header):
    """
    Create a new CSV file with the given name and header. If the file already exists, 
    increment the version number and create a new file.

    Args:
        name (str): The base name of the CSV file.
        header (list): The header row for the CSV file.

    Returns:
        str: The name of the created CSV file.
    """
        
    version = 0                     # Initialize a counter to create unique filenames
    new_name = name            # Initialize the new filename with the original name

    # Check if the file already exists and increment the version number if necessary
    while os.path.isfile(new_name):
        version += 1
        new_name = name.split(".")[0] + "_" + str(version) + ".csv" # Modify the filename to create a new version
    
        # check if file already exists to prepare a fresh new file to prevent using existing file with different structure and data
    with open(new_name,
            mode="w",
            encoding="UTF-8",
            newline=""  # None
        ) as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
                
    return new_name


# Function to write the election results to the CSV file
def write_result(file_csv, header, results):
      
    with open(file_csv,
        mode="a",
        encoding="UTF-8",
        newline=""  # None
    ) as file:   
        writer = csv.writer(file, delimiter=",")
         # Loop through each row of results
        for i in range(0, len(results[0])-1):
            insert = []
            insert.append(results[0][i])   # code
            insert.append(results[1][i])   # location
            insert.append(results[2][i])   # registered
            insert.append(results[3][i])   # envelopes
            insert.append(results[4][i])   # valid
            dict = results[5][i]        # Get the dictionary of votes for each party
            # Loop through each party in the header and add the corresponding vote count
            for vote in header:                     
                if vote in dict:
                    insert.append(dict[vote])       # vote for the given party according to the header in the file
            writer.writerow(insert)                 # Write the row to the CSV file


# ----- MAIN --------------------------------------------------------------------------------------------------------------

# This part of the code runs the main function if the script is executed directly
if __name__ == "__main__":
    main()


