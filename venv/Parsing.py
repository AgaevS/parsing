import requests
from bs4 import BeautifulSoup

url = "https://petrovich.ru/catalog/"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
reg = requests.get(url, headers=headers)
src=reg.text
print(src)
with open("index.html", "w", encoding='utf-8') as file:
   file.write(src)

# with open("index.html", "w", encoding='utf-8') as file:
#    file.write(src)