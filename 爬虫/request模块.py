# import requests
# from urllib.parse import urlencode

# keyword = input('>>:').strip()

# respose = requests.get(
#     'https://www.baidu.com/s?',
#     params={
#         'wd': keyword,
#         'pn': 20
#     },
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
#     },)
# print(respose.status_code)
# with open('a.html', 'w', encoding='utf-8') as f:
#     f.write(respose.text)


import requests
from urllib.parse import urlencode


respose = requests.get(
    'https://github.com/settings/profile',
    params={
    },
    headers={
        # 'Cookie': '_device_id=e07c35bf59538af086f939c71e9eba31; _octo=GH1.1.1604661933.1610768511; has_recent_activity=1; user_session=E7ywKmXpGUAhwdzcYcS83N1X7GqA_DbrYFZufdv44xngB8Ks; __Host-user_session_same_site=E7ywKmXpGUAhwdzcYcS83N1X7GqA_DbrYFZufdv44xngB8Ks; logged_in=yes; dotcom_user=Weway-git; _gh_sess=rv6N5x2jVnzWvZukrPPTidZCmPA9bn22nElbnS9qCm4z7jCIPeue%2BnFJwq2Pj42LRWytBTpzks%2FoUuzhDVjeAdk3izfSeD9Su66eiQdGs8eM0%2FSTVNkpQ%2Foqan26lEdBMhURKE0FbJxWm6ZkCctDvbKKxry%2B41UNfYuymFGroal5sBoHz7Tj%2B7fQ4YsDlo6aqQb8tqD7yDLRInimKPPjxqHhkP4gdE9BCCSur0j13PasfMiQtBZG5AZDe842FsaT%2BhJaw5Ic0ZVn%2FDI1sNlA3Wi6q%2B9ndaoutQMCLm8AVirhmrGzLukf4%2BD0JB6nM25XeUx8vXK3RCC5Y32gblh%2Bw6rawveR8slYPpcz4ZJlZ0v%2BeI%2BF7fRGb6tlilY1Wl21PmsDf9z6TmKXk8cEmXYMKgD4N2%2BTE9O9VXOW08YB4xA4R%2BT6TPRYtqSh1wZG0MV7w76d26JS4sY7IHK1g%2BwtKrTFvA76VC%2FRxrinlwHyeA71tdooR3qzEwYPK4xEUilPOhtKthJedJ1%2FnR7F%2BQ%2Fh%2BdOS5l1Il6u6OarjWXvvFF4992i1qlgRXJCSLPtB%2BwWcpeeKlc5ZmDSYq4SEKsIbA%2Fr2iw%2FPtl2wjI5iqQxhwn5dyxMQjSCNWi65ttLzHv2HIKAbddwvzdSgQK1wICWBNOwemWJGg6v2PCot3WGi2wTzrCTFqngAK8bgS%2BS3fng7sUIw6iF0vWYTnEIPHBM5VsHi0XDMnt1vQUTQbSrhEIn7xX0F40ZGWrZjfK74vxVRlmYfduHts9GqTah%2BFwM8PuFjTocpZXvF4Ex25bl7kqoWYP0HrZ9ViqvAEtUFqPKtAIZVstzYJbXJlRttGOcXHP%2Fq2mZ9EiEWvmetmeevUVEH%2BErSt%2FuZCpptlTyL41lAcmRwjMcGyOxTnId7U7zrArcL7YsFpAG%2Bhdp5bqjPEBw%3D--gFTKT%2F7kcxGphH20--mOePuArhtwSpYVeQDOPdjQ%3D%3D',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
    },
    cookies={
        'Cookie': '_device_id=e07c35bf59538af086f939c71e9eba31; _octo=GH1.1.1604661933.1610768511; has_recent_activity=1; user_session=E7ywKmXpGUAhwdzcYcS83N1X7GqA_DbrYFZufdv44xngB8Ks; __Host-user_session_same_site=E7ywKmXpGUAhwdzcYcS83N1X7GqA_DbrYFZufdv44xngB8Ks; logged_in=yes; dotcom_user=Weway-git; _gh_sess=rv6N5x2jVnzWvZukrPPTidZCmPA9bn22nElbnS9qCm4z7jCIPeue%2BnFJwq2Pj42LRWytBTpzks%2FoUuzhDVjeAdk3izfSeD9Su66eiQdGs8eM0%2FSTVNkpQ%2Foqan26lEdBMhURKE0FbJxWm6ZkCctDvbKKxry%2B41UNfYuymFGroal5sBoHz7Tj%2B7fQ4YsDlo6aqQb8tqD7yDLRInimKPPjxqHhkP4gdE9BCCSur0j13PasfMiQtBZG5AZDe842FsaT%2BhJaw5Ic0ZVn%2FDI1sNlA3Wi6q%2B9ndaoutQMCLm8AVirhmrGzLukf4%2BD0JB6nM25XeUx8vXK3RCC5Y32gblh%2Bw6rawveR8slYPpcz4ZJlZ0v%2BeI%2BF7fRGb6tlilY1Wl21PmsDf9z6TmKXk8cEmXYMKgD4N2%2BTE9O9VXOW08YB4xA4R%2BT6TPRYtqSh1wZG0MV7w76d26JS4sY7IHK1g%2BwtKrTFvA76VC%2FRxrinlwHyeA71tdooR3qzEwYPK4xEUilPOhtKthJedJ1%2FnR7F%2BQ%2Fh%2BdOS5l1Il6u6OarjWXvvFF4992i1qlgRXJCSLPtB%2BwWcpeeKlc5ZmDSYq4SEKsIbA%2Fr2iw%2FPtl2wjI5iqQxhwn5dyxMQjSCNWi65ttLzHv2HIKAbddwvzdSgQK1wICWBNOwemWJGg6v2PCot3WGi2wTzrCTFqngAK8bgS%2BS3fng7sUIw6iF0vWYTnEIPHBM5VsHi0XDMnt1vQUTQbSrhEIn7xX0F40ZGWrZjfK74vxVRlmYfduHts9GqTah%2BFwM8PuFjTocpZXvF4Ex25bl7kqoWYP0HrZ9ViqvAEtUFqPKtAIZVstzYJbXJlRttGOcXHP%2Fq2mZ9EiEWvmetmeevUVEH%2BErSt%2FuZCpptlTyL41lAcmRwjMcGyOxTnId7U7zrArcL7YsFpAG%2Bhdp5bqjPEBw%3D--gFTKT%2F7kcxGphH20--mOePuArhtwSpYVeQDOPdjQ%3D%3D',
    }
)
print(respose.status_code)
print('weway' in respose.text)
