#!/usr/bin/python
# -*- Coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import codecs
import json
import re

def get_data(mercari_id):
    """
    メルカリのidから商品の情報を取得します
    https://mercari.com/jp/items/ここのid/
    """
    mercari_url = f"https://mercari.com/jp/items/{mercari_id}"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    r = requests.get(mercari_url,headers={'User-Agent':user_agent})
    soup = BeautifulSoup(r.text, "html.parser")
    responce = {
        "id" : mercari_id,
        "title" : get_title(soup),
        "image" : get_image(soup),
        "explamation" : get_explamation(soup),
        "price" : get_price(soup),
        "url" : f"https://mercari.com/jp/items/{mercari_id}"
    }
    with codecs.open("search_result.json","w", "utf-8") as f:
        json.dump(responce, f, indent=4, ensure_ascii=False)
    return responce

#商品の画像を取得
def get_image(page_data):
    url_list = []
    images = page_data.find_all('img',class_='owl-lazy')
    pattern = "https?://"
    for url in str(images).split('"'):
        if re.match(pattern,url):
            url_list.append(url)
    return url_list

#商品のタイトルを取得
def get_title(page_data):
    title = page_data.find(class_='item-name')
    return title.get_text()

#商品の説明文を取得
def get_explamation(page_data):
    explamation = page_data.find(class_='item-description-inner')
    return explamation.get_text()

#商品の値段の取得
def get_price(page_data):
    price = page_data.find(class_='item-price bold')
    return price.get_text()