# import requests
# response=requests.get('http://www.google.com')
# print(response.text)#gives code of google.com

import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"#url to access page
r = requests.get(url)
print(r.text)#gives full code of the above url


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())#uses BeautifulSoup to format and arrange the code properly
for heading in soup.find_all("h2"):
  print(heading.text)#print all the h2 headings used in the code
