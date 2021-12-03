import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
bl = "https://www.tokopedia.com/p/handphone-tablet/handphone"
res = requests.get(bl, headers=header)
html = BeautifulSoup(res.content, "html.parser")
rows = html.find("div", class_="bk6tzz e1nlzfl3")
divs = rows.findAll("div", {"class": "89jnbj"})

lst_title = []
lst_img = []
lst_rating = []
lst_harga = []
lst_store = []
lst_link = []

for div in divs:
    title = div.find("div", class_="1bjwylw").text
    img = div.find("div", class_="t8frx0").text
    rating = div.find("div", class_="153qjw7").text
    harga = div.find("div", class_="o5uqvq").text
    store = div.find("div", class_="vbihp9").text
    link = div.a.get("href")
    lst_title.append(title.text.strip())
    lst_img.append(img.text.strip())
    lst_rating.append(rating.text.strip())
    lst_harga.append(harga.text.strip())
    lst_store.append(store.text.strip())
    lst_link.append(link.text.strip())

df = pd.DataFrame({"Judul ": lst_title, "Harga ": lst_harga, "Store ": lst_store,
                   "Rating ": lst_rating, "Gambar ": lst_img, "Link ": lst_link})
df.to_csv('toped.csv', index=False, encoding='utf-8')
