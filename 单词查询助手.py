import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0'
}
url = 'https://fanyi.baidu.com/sug'
kw = input("请输入要查询的单词：")
data = {
    'kw': kw
}
res = requests.post(url, headers=headers, data=data).json()
result = res['data']
if not result:
    print("拼写错误，查询失败！")
for item in result:
    word = item['k']
    meaning = item['v']
    print("单词", word)
    print("释义", meaning)