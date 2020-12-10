# Importing flat files from the web -
from urllib.request import urlretrieve
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
print(url)
urlretrieve(url,'winequality-white.csv')

# Example2 - Import Red Wine Data from Web
import pandas as pd
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# save file locally -
urlretrieve(url,'winequality-red.csv')
# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv',sep=';')
print(df.head())

import matplotlib.pyplot as plt
# Opening and reading flat files directly from the web -
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# read file into Pandas dataframe
df = pd.read_csv(url,sep =';')
print(df.head())
# plot a histogram out of first column of df -
pd.DataFrame.hist(df.loc[:,['fixed acidity']])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('çount')
plt.show()


# Importing non-flat files from the web -
import xlrd
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
# Read in all sheets of Excel file: sheet_name = None lets import of all sheets
xls = pd.read_excel(url,sheet_name = None)
# Print the sheet names to the shell
print(xls.keys())
# Print the head of the first sheet (using its name, NOT its index)
print(xls['1700'].head())

### HTTP requests to import files from the web -
# GET requests using urllib -
# To extract HTML from the wikipedia homepage:-
from urllib.request import urlopen,Request
# specify the url
url = "https://www.wikipedia.org/"
# package the GET request using the function Request
request = Request(url)
# send the request & catch the response using urlopen
response = urlopen(request)
# use the returned HTML response object using the read() method; read method converts the response to get HTML as a string
html = response.read()
# close the response
response.close()

print(html)


# GET requests using Requests package -
import requests
url = "https://www.wikipedia.org/"
r = requests.get(url)
text = r.text
print(text)


# Import packages
from urllib.request import urlopen,Request
# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"
# This packages the request: request
request = Request(url)
# Sends the request and catches the response: response
response = urlopen(response)
# Print the datatype of response
print(type(response))
# Be polite and close the response!
response.close()

# Scraping the web in Python - using BeautifulSoup
from bs4 import BeautifulSoup
# Example 1 -
url = 'https://www.crummy.com/software/BeautifulSoup/'
r = requests.get(url)
html_doc = r.text
# prettify the HTML and then extract the text
soup = BeautifulSoup(html_doc)
print(soup.prettify())


# Example 2 -
# Specify url: url
url = 'https://www.python.org/~guido/'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Extracts the response as html: html_doc
html_doc = r.text
# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)
# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()
# Print the response
print(pretty_soup)

# BeautifulSoup: getting the title of HTML page -
guido_title = soup.title
print(guido_title)
# getting the text of the HTML page
guido_text = soup.get_text()
print(guido_text)

# BeautifulSoup: getting the hyperlinks -
# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))