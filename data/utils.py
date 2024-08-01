from datetime import datetime
import requests
import time
from log_config import logger
from config import CONFIG
from requests import RequestException

# github token扩充访问速率
TOKEN = CONFIG.TOKEN

headers = {
    'Authorization': f'token {TOKEN}',
    'Connection': 'close'
}

# 发送HTTP请求并返回响应
def send_request(url, headers=None, params=None, message=None):
    time.sleep(0.2)
    try:
        response = requests.Session().get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        return response
    except RequestException as e:
        logger.error("%s %s", message, e)
        return None

#查询location获取用户
def location_users(location, page, since, until):
    url = "https://api.github.com/search/users"
    query = f"location:{location} created:{since}..{until}"
    params = {
        "q": query,
        "page": page,
        "per_page": 100
    }
    message = f"获取{location}用户失败:"
    response = send_request(url, headers, params, message)
    if response:
        return response.json()
    return None

#查询用户项目信息
def user_repos(username, page):
    url = "https://api.github.com/search/repositories"
    query = f"user:{username} stars:>=100"
    params = {
        "q": query,
        "page": page,
        "per_page": 100
    }
    message = "获取用户项目失败:"
    response = send_request(url, headers, params, message)
    if response:
        return response.json()
    else:
        return None

#查询用户详细信息
def user_details(username):
    url = f"https://api.github.com/users/{username}"
    message = "获取用户信息失败:"
    response = send_request(url, headers, message)
    if response:
        return response.json()
    else:
        return None

# 填入用户具体信息
def get_user_info(details):
    return {
        "作者昵称": details.get('login'),
        "作者姓名": details.get('name'),
        "作者所在地": details.get('location'),
        "作者粉丝数": details.get('followers')
    }

# 填入项目具体信息
def get_repo_info(repo):
    return {
        "项目名称": repo.get('name'),
        "项目地址": repo.get('html_url'),
        "项目简介": repo.get('description'),
        "Star数量": repo.get('stargazers_count'),
        "Fork数量": repo.get('forks_count'),
        "开发语言": repo.get('language'),
        "项目大小": repo.get('size'),
        "项目创建时间": datetime.strptime(repo.get('created_at'), '%Y-%m-%dT%H:%M:%SZ')
    }


