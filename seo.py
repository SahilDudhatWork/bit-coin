
# Import libraries
from bs4 import BeautifulSoup
import requests
  
# set the url to perform the get request
URL = 'https://preview.themeforest.net/item/xeco-ico-crypto-landing-wordpress-theme/full_screen_preview/48079009?_ga=2.242721863.472869170.1694952683-1712473226.1694952683'
page = requests.get(URL)
  
# load the page content
text = page.content
  
# make a soup object by using
# beautiful soup and set the markup as html parser
soup = BeautifulSoup(text, "html.parser")
  
# open the file in w mode
# set encoding to UTF-8
with open("output.html", "w", encoding = 'utf-8') as file:
    
    # prettify the soup object and convert it into a string
    file.write(str(soup.prettify()))