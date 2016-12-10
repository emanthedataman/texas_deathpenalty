from bs4 import BeautifulSoup

import requests


url = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'
response = requests.get(url)
html = response.text

#things I want from the first page: execution number and link to full bio

soup = BeautifulSoup(html, "lxml")
table = soup.find('table')
links = table.findAll('a', href=True, text='Offender Information')

for link in links:
    print link['href']
