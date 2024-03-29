from bs4 import BeautifulSoup
from time import sleep
from urlparse import urlparse
import requests
import random

url = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'
headers = ['Name', 'TDCJ Number', 'Date of Birth', 'Date Received', 'Age (when    Received)', 'Education Level (Highest Grade Completed)', 'Date of Offense', 'Age (at the time    of Offense)', 'County', 'Race', 'Gender', 'Hair Color', 'Height', 'Weight', 'Eye Color', 'Native County', 'Native State']

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
    

def scrape_off_info(soup, headers):
    
    i = 1
    
    table = soup.find('table', {'class', 'tabledata_deathrow_table'})
    td_tags = table.findAll('td')
    
    for td_tag in td_tags:
        if td_tag.text not in headers and len(td_tag.text) > 1:
            print td_tag.text
            
            






#         text = td_tag.text
#         print text

        
path = get_url_path(url)
soup = cache_to_soup(url, path)
links = scrape_links(soup)


for link in links[0:3]:
    file_path = get_url_path(link)
    soup = cache_to_soup(link, file_path)
    scrape_off_info(soup, headers)


    
    
    