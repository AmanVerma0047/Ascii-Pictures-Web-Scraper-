# Author Kiri

import requests
from bs4 import BeautifulSoup

category = input("Enter Category(e.g.animals):")

get_cat = f"https://www.asciiart.eu/"
cat_response = requests.get(get_cat)

filter_cat = BeautifulSoup(cat_response.text,"html.parser")

all_category = [a.get_text(strip=True) for a in filter_cat.select("#directory ul li a")]

if category.capitalize() not in all_category:
    print("No Category Found!")

tp = input("Enter Type:(e.g.cats)")


get_tp = f"https://www.asciiart.eu/{category}/"
tp_response = requests.get(get_tp)

filter_tp = BeautifulSoup(tp_response.text,"html.parser")

all_tp = [a.get_text(strip=True) for a in filter_tp.select("#directory ul li a")]

if tp.capitalize() not in all_tp:
    print("No Type Found!")


url = f"https://www.asciiart.eu/{category}/{tp}"
response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")

ascii_blocks = soup.find_all("pre")

for block in ascii_blocks:
    print(block.get_text())
    print("-" * 40)
