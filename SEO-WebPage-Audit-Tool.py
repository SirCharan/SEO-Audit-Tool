#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
driver = webdriver.Chrome("D:/chromedriver_win32\chromedriver.exe")


# In[3]:


page=input()
driver.get(page)
content = driver.page_source
soup = BeautifulSoup(content)


# Word Count Text
# 

# In[5]:


heads=['h1','h2','h3','h4','h5','h6']
sum=0
for a in soup.findAll('p'):
    sum=sum+len(a.text.split(' '))
for j in range(len(h)):
    for a in soup.findAll(h[j]):
        sum=sum+len(a.text.split('>')[0].split(' '))
print(sum)


# Text To HTML Ratio

# In[7]:


suma=0
for a in soup.findAll():
    suma=suma+len(a.text.split(' '))         
print(sum/suma*100)


# Meta Tags

# In[8]:


itemn=["description","title","keywords"]
itemna=[1,1,1]
for j in range(len(itemn)):
    for a in soup.findAll('meta',attrs={'name':itemn[j]}):
        itemna[j]=0
        print("\nMeta "+itemn[j])
        print(a.get('content'))
    if(itemna[j]):
        print("\nMeta "+itemn[j]+" Missing")


# Open Graph Protocol Tags

# In[10]:


itemp=["og:title","og:description"]
itempa=[1,1]
for j in range(len(itemp)):
    for a in soup.findAll('meta',attrs={'property':itemp[j]}):
        itempa[j]=0
        print("\nOG "+itemp[j])
        print(a)
    if(itempa[j]):
        print("\nOG "+itemn[j]+" Missing")
        


# Header Tags-

# In[11]:


h=['h1','h2','h3','h4','h5','h6']
ha=[1,1,1,1,1,1]
for j in range(len(h)):
    print("\n")
    print(h[j])
    for a in soup.findAll(h[j]):
        print(a.text)
        ha[j]=0
    if(ha[j]):
        print("No "+ h[j])


# Image Alt Text Missing-

# In[13]:


co=0
coo=0
for a in soup.findAll('img'):
    co=co+1
    if(a.get('alt')):
        coo=coo+1
#     print(a.get('alt'))
print("Total Images On Page-")
print(co)
print("No Alt tags-")
print(co-coo)


# All The links on the page-

# In[17]:


links=[]
i=0
sub='https://henryharvin'
suba='https://www.henryharvin.com/'
for a in soup.findAll('a'):
    b=a.get('href')
    d=b.count(suba)+b.count(sub)
    if(d):
        links.append(b)
        print(links[i])
        i=i+1


# In[ ]:




