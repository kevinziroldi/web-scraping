import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.cnbc.com/wars-and-military-conflicts/')
source = page.content
soup = BeautifulSoup(source, 'lxml')

urls = soup.find_all('a')

links = []

for url in urls:
    if 'href' in url.attrs and 'https' in url.attrs['href']:
        links.append(str(url.attrs['href']))
        links.append('\n')
        #print(str(url.attrs['href']))
# print(links)

file = open('links_guerra.txt', 'w')
for link in links:
    file.write(link)
file.close()