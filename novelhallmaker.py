import requests
import time
str1=""
x=str1.split(",")
f= open("konoha-hypocrite.txt", "a+", encoding="utf-8")
for i in range(0,len(x)):
  from urllib.request import Request, urlopen
  from bs4 import BeautifulSoup

  url = f"{x[i]}"
  req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'})

  web_byte = urlopen(req).read()
  soup = BeautifulSoup(web_byte, features="html.parser")

  # kill all script and style elements
  for script in soup(["script", "style"]):
    script.extract()  # rip it out

  # get text
  text = soup.get_text()

  # break into lines and remove leading and trailing space on each
  lines = (line.strip() for line in text.splitlines())
  # break multi-headlines into a line each
  chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
  # drop blank lines
  text = '\n'.join(chunk for chunk in chunks if chunk)
  sl = text.find("Turn off\nReset")
  sm= text.find("Chapter")
  sub_list = ["", ]
  for sub in sub_list:
    text = text.replace(sub, ' ')
  res = " ".join(text.split())
  f.write(text[sm:sm+15])
  f.write(text[sl+14:-362])

