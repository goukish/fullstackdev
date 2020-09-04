# Goutham Naveen Babu - Full stack Challenge

import requests
from bs4 import BeautifulSoup     # imports
import csv

file = open('output.csv', 'w')     # set up csv output file
writer = csv.writer(file)
writer.writerow(['Questions'])

page = requests.get('https://www.cheatsheet.com/gear-style/20-questions-to-ask-siri-for-a-hilarious-response.html/')
soup = BeautifulSoup(page.content, 'html.parser')
row = soup.find_all('h2')        # finding only the questions in web page
writer.writerow([row])           # writing to csv




