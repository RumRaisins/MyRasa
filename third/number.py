import requests
import json
from requests import (
    ConnectionError,
    HTTPError,
    TooManyRedirects,
    Timeout
)


API = r"https://www.kuaidi100.com/chaxun?com=[]&nu=[]"


if __name__ == '__main__':
    result = requests.get(API, params={"com":"zhongtong", "nu":78169856157631})
    print(result.json())