# import pandas as pd
import pymysql
import json
import requests
con = pymysql.connect(host='114.141.150.80', user='root',
                      passwd='qiang666', db='python_api', port=3307, charset='utf8')

# 创建游标对象
cur = con.cursor()

cur.execute(' CREATE TABLE tianqi (id int not null auto_increment primary key,date int ,date2 varchar(20),history_rain varchar(20),history_max int,history_min int,tmax varchar(10),tmin varchar(10),time varchar(20),w1 varchar(20),wd1 varchar(20),alins varchar(20),als varchar(20))')


class Weather():

    url = "https://dashboard.17zhiliao.work"
    login_api = "/api/operation/login"


    def __init__(self):
        pass

    def get_token(self):
        r = requests.post(url+login_api, json={
            "mail": "luoshengying@17zhiliao.com",
            "password": "Shengying7132"
        })
        x = json.loads(r.text)
        print(x)
        data_key = "authorization"
        token = x[data_key]
        print("token is : ", token)
        project_list_api = "/api/delivery/search?offset=0&limit=20"
        headers = {
        'Authorization': "Bearer "+token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        }
        return token
    def get_data(self):
        Weather.get_token()
        project_list_api = "/api/delivery/search?offset=0&limit=20"
        headers = {
            'Authorization': "Bearer "+token,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        datas = '{"completedAt":{"$exists":false},"extension.platform._id":"5cb3ec09a3399e0ea720fb54"}'
        r = requests.post(url+project_list_api, data=datas, headers=headers)
        print(r)
        project_list = json.loads(r.text)
        print(project_list)

    def get_info(self):
                date = data['date']
                date2 = data['nlyf'] + data['nl']
                history_rain = data['hgl']
                history_max = data['hmax']
                history_min = data['hmin']
                tmax = data['max']
                tmin = data['min']
                time = data['time']
                w1 = data['w1']
                wd1 = data['wd1']
                alins = data['alins']
                als = data['als']

            # 先把去重的数据存储到列表all_info
            info = (date, date2, history_rain, history_max,
                    history_min, tmax, tmin, time, w1, wd1, alins, als)
            if info not in self.all_info:
                self.all_info.append(info)
        # 把数据存到sqlite

    def store_pymysql(self):
        self.get_data()
        for one_info in self.all_info:
            cur.execute(' INSERT INTO tianqi (date,date2,history_rain,history_max,history_min,tmax,tmin,time,w1,wd1,alins,als) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', one_info)
            con.commit()


    # 新建列表，用来存储获取的数据
all_info = []

# 获取一年的天气数据
# def get_data(self):

# month = ['01', '02', '03', '04', '05', '06',
#          '07', '08', '09', '10', '11', '12']
# for i in month:
#     url = 'http://d1.weather.com.cn/calendar_new/' + str(year) + '/101280601_' + str(year) + str(
#         i) + '.html?_=1496558858156'
#     html = requests.get(url, headers=self.headers).content
#     global datas
#     datas = json.loads(html[11:])
#     self.get_info()

# 获取天气的具体数据


if __name__ == '__main__':
    year = '2017'
    tianqi = Weather()
    tianqi.store_pymysql()
    # 关闭数据库连接
    con.close()
