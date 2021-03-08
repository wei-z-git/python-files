import json
import requests

url = "https://dashboard.17zhiliao.work"

login_api = "/api/operation/login"
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
    'Authorization':"Bearer "+token,
    'Accept':'application/json',
    'Content-Type':'application/json'
}
datas='{"completedAt":{"$exists":false},"extension.platform._id":"5cb3ec09a3399e0ea720fb54"}'
r = requests.post(url+project_list_api, data=datas, headers=headers)
print(r)
project_list = json.loads(r.text)
print(project_list

# num=len(project_list)
# print("项目总数: ", num)
# project_list_api = "/group"
# headers = {}
# headers['X-Authorization'] = token
# r = requests.get(url+project_list_api, headers=headers)
# project_list = json.loads(r.text)
# num=len(project_list)
# print("count ", num)