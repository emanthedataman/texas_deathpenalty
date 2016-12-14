from bs4 import BeautifulSoup
from time import sleep
from urlparse import urlparse
import requests
import random

url = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'


def get_url_path(url):
    '''checks url and determines the appropriate path for cache'''
    
    parsed_url = urlparse(url)
    file_name = parsed_url.path.split('/')[-1]
    
    if 'dr_executed_offenders' in file_name:
        file_path = '../cache/all_offenders/' + file_name
    else:
        file_path =  '../cache/indiv_offenders/' + file_name 
    
    return file_path


def cache_to_soup(url, file_path):
    '''creates cache from the url'''
    
    min_sec = 0.5
    max_sec = 2.7
    
    try:
        print 'Reading file...' + file_path
        read_cache = open(file_path, 'rb')
        soup = BeautifulSoup(read_cache, "lxml")
        read_cache.close()

    except IOError:
    
        print 'Writing file... ' + file_path
        
        response = requests.get(url)
        sleep(random.uniform(min_sec, max_sec))
        html = response.text
        
        write_cache = open(file_path, 'wb')
        write_cache.write(html.encode('utf-8'))
        soup = BeautifulSoup(html, "lxml")
        write_cache.close()
        
    return soup

def scrape_links(soup):
    
    root_url = 'http://www.tdcj.state.tx.us/death_row/'
    inmate_links = []
    
    table = soup.find('table')
    links = table.findAll('a', href=True, text='Offender Information')
    for link in links:
        inmate_link = root_url + link['href']
        inmate_links.append(inmate_link)
          
    return inmate_links
    
        
        
path = get_url_path(url)
soup = cache_to_soup(url, path)
links = scrape_links(soup)
print links




    



  
# #things I want from the first page: execution number and link to full bio
# soup = url_to_soup(url)
# table = soup.find('table')
# links = table.findAll('a', href=True, text='Offender Information')
# 
# inmate_links = []
# 
# for link in links:
#     inmate_link = root_url + link['href']
#     inmate_links.append(inmate_link)
#     
# 
# for inmate in inmate_links[0:1]:
#     sleep(random.uniform(min_sec, max_sec))
#     soup = url_to_soup(inmate)
#     
#     table = soup.find('table', {'class','tabledata_deathrow_table'})
#     print table
    
    
    