from bs4 import BeautifulSoup

with open("https://www.victoriassecret.com/us/index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

