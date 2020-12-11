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



# Introduction to APIs and JSONs -
import json
with open('snake.json','r') as json_file:
    json_data = json.load(json_file)
type(json_data)

# Example 2 -
with open(r'D:\Learning\UCD Professional Academy\Course 1 - Professional Certificate in Data Analytics\Python Practice\world_countries.json') as file:
    data = json.load(file)
print(type(data))


## APIs and interacting with the world wide web -
# OMDB Movie API
import requests
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'
# Package the request, send the request and catch the response:
r = requests.get(url)
# Decode the JSON data into a dictionary: json_data
json_data = r.json()
for key,value in json_data.items():
    print(key + ':',value)
print(r.text)

# Checking out the Wikipedia API - (Wikipedia page for Pizza)
import requests
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'
# Package the request, send the request and catch the response:
r = requests.get(url)
# Decode the JSON data into a dictionary: json_data
json_data = r.json()
# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)


# The Twitter API and Authentication -
# Example -
# Import package
import tweepy

# Store OAuth authentication credentials in relevant variables
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler('nZ6EA0FxZ293SxGNg8g8aP0HM','fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i' )

auth.set_access_token("1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy","X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx")

## Streaming tweets -
# Initialize Stream listener
l = MyStreamListener()

# Create your Stream object with authentication
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
stream.filter(['clinton','trump','sanders','cruz'])