import requests
import re
res = requests.get(url='https://github.com/login',
                   headers={
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',
                   },
                   )

authenticity_token = re.findall(
    'name="authenticity_token".*?value="(.*?)"', res.text, re.S)[0]
# requests.post(url='xx',)
