# PROJECT 3 Election Scraper (`project3_election_scraper.py`)

This is the third project of the "Data Analyst with Python" academy from Engeto company.

## Short Brief

The main purpose of this script is to gather data from a given link (script argument 1) about the results of the 2017 election. 

Here is the link to the main page of the results from **20.10 - 21.10.2017**: [https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

1. You can choose any district and click on "X" in the column "Výběr obce".
2. Then, copy the link from the browser's command line. For example, for **"Praha"**:
   [https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100)

This is the **first argument** of the script.

The detailed data will be loaded into your **CSV file** (the **second argument** of the script).

## Installation of Libraries

This script uses third-party libraries that you need to install. You can find the list of used libraries in the `requirements.txt` file. A new virtual environment is recommended for installing the libraries.

To install the libraries, use this command:

```bash
$ pip3 --version  
$ pip3 install -r requirements.txt
```

## How to Launch the Project/Script

You need 2 arguments to launch the project from the command line:
<ul>
    <li>Argument 1: Link to the district</li>
    <li>Argument 2: Name of the file to store the data</li>
</ul>

Example Command to Launch the Script

```bash
python project3_election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3205" "election_data.csv"
```

## Progress of the Program

When you run the script, you will see the following steps:

```bash
Loading data of municipality codes, locations, and links to the election details of municipalities...
DONE
Loading detailed data of each municipality code...
DONE
The file name already exists. The name of the created file is election_data_2.csv
Data has been written into the file: election_data_2.csv
```

Example Data in the File:

```bash
code,location,registered,envelopes,valid,Česká str.sociálně demokrat., ...
566756,Bdeněves,510,367,365,17,1,42,4,0,1,21,2,50,44,3,0,2
558656,Bezvěrov,551,257,254,18,5,17,2,1,0,28,1,9,9,3,0,0
530239,Bílov,58,33,32,2,0,10,0,0,0,3,0,1,1,2,0,0
558672,Blatnice,677,398,395,36,7,46,3,1,2,31,0,32,32,1,0,0
566764,Blažim,52,27,27,1,0,1,1,0,0,6,0,0,2,0,0,0
...
```

### Other Examples:
Example 1: Písek
```bash
python project3_election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3104" "election_data.csv"
```
Example 2: Plzeň-sever
```bash
python project3_election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3205" "election_data.csv"
```
Example 3: Praha
```bash
python project3_election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100" "elections_praha.csv"
```
