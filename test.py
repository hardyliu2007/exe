import urllib.request
from lxml import etree
headers = {
        'Host': 'music.163.com',
        'Referer': 'https://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }
url = "https://music.163.com/#/song?id=418602088"
resp = urllib.request.urlopen(url)
data = resp.read()
html = etree.HTML(data)
b = html.xpath('//*[@id="auto-id-PXTd3rNCFls0JEgm"]/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div/em')
print(b)
print(html)