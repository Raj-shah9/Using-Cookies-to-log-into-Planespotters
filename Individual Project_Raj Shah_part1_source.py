#!/usr/bin/env python
# coding: utf-8

# In[13]:

## Importing Libraries
from bs4 import BeautifulSoup
import requests
import time

#Accessing the Planespotter login page
session_requests = requests.session()
URL = "https://www.planespotters.net/user/login"
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
page1 = session_requests.get(URL,headers = header)

# Using the cookies that load after a successful login to the page
cookies = page1.cookies.get_dict()
doc1 = BeautifulSoup(page1.content,'html.parser')


input = doc1.find("input", id="csrf")
csrf = input.get("value")
    
input = doc1.find("input", id="rid")
rid = input.get("value")

print(csrf)
print(rid)


# In[127]:

## Defining a function to save the html files
def saveString(html, filename="test.html"):
    try:
        file = open(filename,"w",encoding='utf-8')
        file.write(str(html))
        file.close()
    except Exception as ex:
        print('Error: ' + str(ex))


# In[20]:



## Introducing a sleep time
time.sleep(5)


## Navigating to the second page
res = session_requests.post(URL,
                        data = {"username": "rajshah","password": "Test1234","csrf": csrf,"rid": ""},
                                headers = header,
                                cookies = cookies)

## Getting the cookies from the second page
cookies2 = res.cookies.get_dict()


## Introducing a sleep time
time.sleep(5)

## Parsing the Url and cookies to get the required information
url2 = 'https://www.planespotters.net/member/profile'
page2 = session_requests.get(url2,headers = header, cookies = cookies2)
doc2 = BeautifulSoup(page2.content, 'html.parser')




# In[21]:

## Printing all the cookies and finding if the username exists
print(doc2)
print('')
print('The cookies for the first page are: ' + str(cookies))
print('')
print('The cookies for the second page are: ' + str(cookies2))
print('')
print('The boolean value for the username is : ' + str(bool(doc2.find_all(text = "rajshah"))))

