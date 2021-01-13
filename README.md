### heavy_traffic
城市交通拥堵情况,用flask在网页上地图显示
![](./res/python-qq-group.png)
### [dianziyan_spider](./dianziyan_spider)
- dianziyan_spider.py文件：爬虫读取北京交通电子眼地理数据，生成并存储在csv文件(dianziyan.csv)中  
- Camera_map.py文件：生成地图展示的html文件，因为爬虫的csv数据的底图坐标和电子眼经纬度标准不统一，为了定位更准确，把底图和电子眼经纬度统一规范为高德地图，使用百度经纬度转换成高德经纬度的函数。
