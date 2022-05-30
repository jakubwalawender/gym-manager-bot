import requests

from config.settings import LOGIN_URL
import logging
logger = logging.getLogger(__name__)


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
        res = r.json()
        if 'access_token' not in res:
            logger.debug(f"Getting access token for user {user.name} failed")
            return None
        token = res['access_token']
        return token
    except Exception as e:
        logger.debug(f"Getting access token for user {user.name} failed!. Exception: {e}")
        return None
