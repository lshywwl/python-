# 时间：2020/12/16  16:39
import math
def bdToGaoDe(lat,lon):
    """
    百度经纬度转高德经纬度
    :param lon:
    :param lat:
    :return:
    """
    PI = 3.14159265358979324 * 3000.0 / 180.0
    x = lon - 0.0065
    y = lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * PI)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * PI)
    lon = z * math.cos(theta)
    lat = z * math.sin(theta)
    return lat,lon

# 读取数据，进行转换
import pandas as pd
data=pd.read_csv('dianziyan.csv',encoding='gbk')
for name,row in data.iterrows():
    print(bdToGaoDe(row["纬度"],row["经度"]))

# 将底图换成高德地图，然后将标点转换成电子眼图标：
import folium
from folium import plugins
Camera_map = folium.Map(location=[data['纬度'].mean(), data['经度'].mean()], zoom_start=10,zoom_control='False',
                     tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',attr='AutoNavi')
incidents = folium.map.FeatureGroup()
tooltip ='请点击我查看该点信息'
for name,row in data.iterrows():
    incidents.add_child(
        folium.Marker(            #CircleMarker表示花圆
            [bdToGaoDe(row["纬度"],row["经度"])[0],bdToGaoDe(row["纬度"],row["经度"])[1]],   #每个停车场的坐标
            icon=folium.Icon(color='green', prefix='fa', icon='bullseye')
        )
    )

Camera_map.add_child(incidents)
Camera_map.save('Camera_map2.html')