# メルカリデータ取得api
メルカリの検索apiが欲しかったので作成しました。
<br>スクレイピングをしているだけなので検索に時間がかかります。
<br>また、やりすぎると規制になる可能性もあるので気をつけてください

## データの取得方法
sample.pyのようなコードを自前で用意してください。
<br>検索結果はsearch_result.jsonというものに表示されます。
<br>jsonデータを読み込んで煮るなり焼くなり好きにしてください

## キーワード検索
```python:sample.py
from mercaripy import keyword_search
import json

keyword_search.search_with_keyword("MacBookPro")
with open("search_result.json", "r") as f:
    data = json.load(f)

print(data["1"]["title"])
print(data["1"]["url"])
```

## urlからデータ取得
ここでは https://mercari.com/jp/items/ の後のidみたいなものを入力してください

``` python:sample.py
from mercaripy import get_data
import json

get_data.get_data("m76779507804")
with open("search_result.json","r") as f:
    data = json.load(f)

print(data["title"])
print(data["price"])
print(data["url"])
```

## 終わりに
何かわからないことがあれば[Twitter](https://twitter.com/_kmch4n_)までどうぞ