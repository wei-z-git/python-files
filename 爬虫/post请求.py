import requests
import re
r1 = requests.get(url='https://github.com/login',
                  headers={
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',
                  },
                  )

authenticity_token = re.findall(
    'name="authenticity_token".*?value="(.*?)"', r1.text, re.S)[0]
r1_cookies = r1.cookies.get_dict()
print(r1_cookies)
r2 = requests.post(url='https://github.com/session',
                   headers={
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',
                       'Referer': 'https://github.com/login',
                   },
                   data={

                       'commit': 'Sign in',
                       'authenticity_token': authenticity_token,
                       'login': '1419864987@qq.com',
                       'password': 'wodeyuwen666',
                   },
                   cookies=r1_cookies,

                   )
print(r2.status_code)

requests.get()
