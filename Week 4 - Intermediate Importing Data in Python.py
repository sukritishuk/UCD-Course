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

## Load & explore your Twitter data -
# Import package
import json
# Define file path
tweets_data_path = 'tweets.txt'
# Initialize empty list to store tweets:
tweets_data = []
# Open connection to file
tweets_file = open(tweets_data_path,'r')
# Read in tweets and store in list
for line in tweets_file:
    tweet = json_loads(line)
    tweets_data.append(tweet)
# Close connection to file
tweets_file.close()
# Print the keys of the first tweet dict
print(tweets_data[0].keys())


# Importing Data in Python - Practice
# Example 1 -
from bs4 import BeautifulSoup
import requests
url = 'https://www.python.org/~guido'
r = requests.get(url)
d = r.text
s = BeautifulSoup(d)
print(type(r))

# Example 2 -
import pandas as pd
from urllib.request import urlretrieve
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
urlretrieve(url,'winequality-wh.csv')
data = pd.read_csv('winequality-wh.csv',sep=';')
print(data[['alcohol','quality']].head())


# Example 3 -
import requests
url = ('http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network')
r = requests.get(url)
json_data = r.json()
print(json_data['Awards'])

# Example 4 -
url = 'https://www.python.org/~guido/'
r = requests.get(url)
html_doc = r.text
s = BeautifulSoup(html_doc)
print(s.title)


## Coonect to SQL DB Practice -
# Example - 1
import pymysql
# database connection -
connection = pymysql.connect(host='localhost',user='root',passwd="",database="hospital_info")
cursor = connection.cursor()
# retrieve data from table -
retrieve = "SELECT * FROM doctor;"
# executing the query
cursor.execute(retrieve)
rows = cursor.fetchall()
for row in rows:
    print(row)
# commit the connection -
connection.commit()
# close the connection -
connection.close()

# Example - 2
connection = pymysql.connect(host='localhost',user='root',passwd="",database="hospital_info")
cursor = connection.cursor()
# getting all tables present in hospital_info DB -
cursor.execute("SHOW TABLES;")
# print all tables in DB -
names_table = cursor.fetchall()
for table in names_table:
    print(table)

# Example - 3
import pandas as pd
connection = pymysql.connect(host='localhost',user='root',passwd="",database="hospital_info")
cursor = connection.cursor()
# getting all tables present in hospital_info DB -
cursor.execute("SELECT * FROM doctor;")
df = pd.DataFrame(cursor.fetchall())
# name the columns and set index column -
df.columns = ['Doctor_Id','Doctor_Name','Hospital_Id','Joining_Date','Speciality','Salary','Experience']
df = df.set_index(['Doctor_Id'])
print(df)


## Scraping the web in Python Practice -
# Scraping the Monster Job Site -
import requests
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
# parse HTML code with BeautifulSoup -
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content,'html.parser')
# print the title of web page -
print(soup.title)
# print the text on the page -
print(soup.get_text())
# iterate through all of the hyperlinks on the page and print their URLs -
for link in soup.find_all('a'):
    print(link.get('href'))
# finding elements by ID & prettifying it -
results = soup.find(id='ResultsContainer')
print(results.prettify())
# find Elements by HTML Class Name - select only the job postings:
job_elems = results.find_all('section', class_='card-content')
print(job_elems)

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    print(title_elem)
    print(company_elem)
    print(location_elem)
    print()

# Extract Text From HTML Elements - using .text
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue   # disregard the problematic element and skip over it
    print(title_elem.text)
    print(company_elem.text)
    print(location_elem.text)
    print()

# Find Elements by Class Name and Text Content
#  job titles in the page are kept within <h2> elements
python_jobs = results.find_all('h2', string='Python Developer')








