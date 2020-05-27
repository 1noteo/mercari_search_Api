#!/usr/bin/python
# -*- Coding: utf-8 -*-
from mercaripy import(
    get_data, keyword_search
)
import codecs
import json

def mercari_search_with_keyword(search_keyword):
    keyword_search.search_with_keyword(search_keyword, num=3)
    #ここのnumを増やせば検索数を増やせる。増やしすぎると遅くなるので注意
    with codecs.open("search_result.json", "r", "utf-8") as f:
        result = json.load(f)
    #result["数字"]で別の検索結果も表示可能
    print(
        f"""
        商品名:{result["1"]["title"]}
        商品画像:{result["1"]["image"][0]}
        商品値段:{result["1"]["price"]}
        商品説明:{result["1"]["explamation"]}
        商品リンク:{result["1"]["url"]}
        """
    )

def get_mercari_info(mercari_id):
    #https://mercari.com/jp/items/ここのid
    get_data.get_data(mercari_id)
    with codecs.open("search_result.json", "r", "utf-8") as f:
        result = json.load(f)
    print(
        f"""
        商品名:{result["title"]}
        商品画像:{result["image"][0]}
        商品値段:{result["price"]}
        商品説明:{result["explamation"]}
        商品リンク:{result["url"]}
        """
    )

mercari_search_with_keyword("キーボード")
get_mercari_info("m76779507804")