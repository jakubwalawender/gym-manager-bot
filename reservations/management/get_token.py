import requests

from config.settings import LOGIN_URL


def get_token(user, password):
    data = {
        "login": user,
        "password": password,
        "facebookid": "undefined"}
    headers = {
        "Accept": "application/json, text/plain, */*",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
        "Host": "stats.fitnessplatinium.pl:13002",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    try:
        r = requests.post(LOGIN_URL, data=data, headers=headers)
        token = r.json()['access_token']
        return token
    except:
        return None