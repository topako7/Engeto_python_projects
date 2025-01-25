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
    """
    Main function that drives the scraping process, handling command-line arguments and calling 
    the scraping functions for districts and municipalities. Writes the results to a CSV file.
    """

    # Check if the correct number of arguments are provided (script name + 2 arguments)
    if len(sys.argv) != 3:
        print("Usage: python project3_election_scraper.py <param1 - link to any district from https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ> <param2 - filename.csv>")
        sys.exit(1)

    # Retrieve the two parameters from the command-line arguments
    url = sys.argv[1]               # The URL of the district page (passed as the first argument)
    election_data = sys.argv[2]     # The name of the CSV file (passed as the second argument)

    #url = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3205" #input static parameter 1 (test)
    #election_data = "election_data.csv" #input static parameter 2 (test)

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
    
    print(f"Loading data of municipality codes, locations and links to the election details of municipalities...")
    
    try:
        html_text = requests.get(url)                                                 # load the html code
        soup_district = BeautifulSoup(html_text.text, 'html.parser')                            # html code + parser type
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the municipality page {url}: {e}")
                               
    #print(soup.prettify())
    main_div = soup_district.find("div", {"id": "inner"})       # find the main part of the text to analyze
    td_tags = main_div.find_all("td", {"class": "cislo"})               # find td tags with class="cislo"
    td_locations = main_div.find_all("td", {"class": "overflow_name"})  # find td tags with class of the location name
    
    for td in td_tags:  
        a_tags = td.find("a")
        links.append(base_url + a_tags['href'])                                                 # save the link to the detail of votes
        codes.append(a_tags.text.strip())                                                       # save the code of the location

    for td in td_locations:
        locations.append(td.text.strip())                                                       # save the name of the location
    print(f"DONE")

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

    print(f"Loading detailed data of each municipality codes...")
    for link in urls:
        try:
            text = requests.get(link)
            text.raise_for_status()  # Raise an exception for invalid responses
            soup_municipality = BeautifulSoup(text.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the municipality page {link}: {e}")
            continue
        
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
        #votes = {name.text.strip(): int(result.text.strip()) for name, result in zip(td_party_name, td_party_votes)}
        votes = {name.text.strip(): int(result.get_text(strip=True).replace('\xa0','')) for name, result in zip(td_party_name, td_party_votes)}

        
        votes_results.append(votes)
    print(f"DONE")
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
        new_name = f"{name.split('.')[0]}_{version}.csv" # Modify the filename to create a new version
    if version > 0: print(f"File name already exists. The name of created file is {new_name}")
    else: print(f"The {new_name} has been created.")
        # check if file already exists to prepare a fresh new file to prevent using existing file with different structure and data
    with open(new_name,
            mode="w",
            encoding="UTF-8",
            newline=""  # None
        ) as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
                
    return new_name


def write_result(file_csv, header, results):
    """
    Write the election results to the specified CSV file.

    Args:
        file_csv (str): The path to the CSV file.
        header (list): The header row for the CSV file.
        results (list): The election data (codes, locations, registered, envelopes, valid, votes).
    """
    
    rows = []
    for i in range(len(results[0])):
        insert = [
            results[0][i],  # Code
            results[1][i],  # Location
            results[2][i],  # Registered voters
            results[3][i],  # Envelopes sent
            results[4][i],  # Valid votes/envelopes
        ]
        party_votes = results[5][i]
        insert.extend([party_votes.get(vote, 0) for vote in header[5:]])  # Get vote counts for each party
        rows.append(insert)

    with open(file_csv, mode="a", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerows(rows)  # Write all rows at once
    print(f"Data has been written into the file: {file_csv}")


# ----- MAIN --------------------------------------------------------------------------------------------------------------

# This part of the code runs the main function if the script is executed directly
if __name__ == "__main__":
    main()


