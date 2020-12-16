import requests
from bs4 import BeautifulSoup
import csv
import json,time
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
}
for page in range(1,4):
    url1='https://www.icauto.com.cn/weizhang/wzd/110000/list_{0}.html'.format(page)
    response=requests.get(url1,headers=header)
    soup=BeautifulSoup(response.text,'html.parser')
    results=soup.find('div',class_='cdz-ccotent').find_all('li')
    for result in results:
        time.sleep(0.5)
        name=result.find('a').text
        index=result.find('span').text.split('：')[1]
        print(name,index)
        url2='https://api.map.baidu.com/?qt=gc&wd={}&cn=北京&ie=utf-8&oue=1&fromproduct=jsapi&res=api&ak=s8sS5dBsZ7bLRi3bcVRAaYMAnqlXoyeo'.format(name)
        print(url2)
        response=requests.get(url2,headers=header)
        print(response.text)
        coord=json.loads(response.text)['content']['coord']
        print(coord)
        url3='http://api.map.baidu.com/geoconv/v1/?coords={}&from=6&to=5&ak=rmEs50SQTeAmkzN6HagxrcCi4Q2PQHfE'.format(str(coord['x'])+','+str(coord['y']))
        response=requests.get(url3,headers=header)
        result=json.loads(response.text)['result'][0]
        print(result)
        lon=result['x']
        lat=result['y']
        with open('dianziyan.csv', 'a+', newline='', encoding='gb18030') as f:
            f_csv = csv.writer(f)
            f_csv.writerow([name, index, lon,lat])
