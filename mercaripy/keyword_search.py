#!/usr/bin/python
# -*- Coding: utf-8 -*-
from bs4 import BeautifulSoup
from . import get_data
import requests
import codecs
import json

def search_with_keyword(keyword, num=5):
    """
    メルカリで検索して情報を取得します
    numで検索数を指定できます
    多すぎると遅い上に規制される確率も上がります
    """
    search_url = f"https://www.mercari.com/jp/search/?keyword={keyword}"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    r = requests.get(search_url,headers={'User-Agent':user_agent})
    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find_all(class_="items-box", limit=num)
    datas  = str(result).split("/")
    result_list = []
    for data in datas:
        if data.startswith("m"):
            if len(data) < 15:
                result_list.append(data)
    make_responce(result_list)

def make_responce(data_list):
    responce = {}
    num = 1
    for data in data_list:
        result = get_data.get_data(data)
        responce[num] = {
            "id"    : result["id"],
            "title" : result["title"],
            "image" : result["image"],
            "explamation" : result["explamation"],
            "price" : result["price"],
            "url"   : result["url"]
        }
        num += 1
    with codecs.open("search_result.json", "w", "utf-8") as f:
        json.dump(responce, f, indent=4, ensure_ascii=False)
