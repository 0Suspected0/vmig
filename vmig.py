import requests
import fake_useragent
from bs4 import BeautifulSoup

#anton.edupcpo@gmail.com
#12345

session = requests.session()
link = "https://vmig.expert/api/auth/login"
#user = fake_useragent.UserAgent().random
user = Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0

header = {
    'User-Agent': user
}

data ={
    '_type': 'LoginFormDTO',
    'login': 'anton.edupcpo@gmail.com',
    'password': '12345'
}

responce = session.post(link, data=data, headers=header)
profile_info = "https://vmig.expert/student"
profile_responce = session.get(profile_info).text

cookies_dict = [
    {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
    for key in session.cookies
]

session2 = requests.session()
for cookies in cookies_dict:
    session2.cookies.set(**cookies)

session2.get(profile_info, headers=header)
print(responce.text)