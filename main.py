from bs4 import BeautifulSoup

import requests


url = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'

requests.get(url)