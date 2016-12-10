from bs4 import BeautifulSoup
from time import sleep

import requests
import random


root_url = 'http://www.tdcj.state.tx.us/death_row/'
url = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'

min_sec = 0.5
max_sec = 2.7




def url_to_soup(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    
    return soup

 
#things I want from the first page: execution number and link to full bio
soup = url_to_soup(url)
table = soup.find('table')
links = table.findAll('a', href=True, text='Offender Information')

inmate_links = []

for link in links:
    inmate_link = root_url + link['href']
    inmate_links.append(inmate_link)
    

for inmate in inmate_links[0:1]:
    sleep(random.uniform(min_sec, max_sec))
    soup = url_to_soup(inmate)
    
    table = soup.find('table', {'class','tabledata_deathrow_table'})
    print table
    
    
    