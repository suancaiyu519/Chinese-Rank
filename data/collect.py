from data.utils import location_users, user_repos, user_details, get_user_info, get_repo_info
from data.save import save_to_database
from log_config import logger
from config import CONFIG
from datetime import timedelta

def data_collect(start, end, session):
    location1 = CONFIG.location1
    location2 = CONFIG.location2
    days = 256
    # 由于github只提供前1000条信息，所以通过设置创建账号的时间区间控制用户数量在1000以内
    since = start
    # 设置一个时间段
    until = since + timedelta(days=days)
    if until > end:
        until = end
    # 时间段大于当前时间则停止
    while since < end:
        page = 1
        result = location_users(location1, location2, page, since.strftime('%Y-%m-%d'), until.strftime('%Y-%m-%d'))
        # 获取失败重试
        if not result:
            continue
        # 判断该时间段内用户数量是否在1000以内
        if 0 < result.get("total_count") <= 1000:
            while True:
                # 获取指定location的用户
                result = location_users(location1, location2, page, since.strftime('%Y-%m-%d'), until.strftime('%Y-%m-%d'))
                # 获取失败重试
                if not result:
                    continue

                # 用户全部获取则退出
                if not result.get('items', []):
                    break

                # 用户基本信息
                users = []
                users.extend(result.get('items', []))

                # 项目信息
                repos_info = []

                # 获取用户详细信息
                index = 0
                while True:
                    # 如果索引超出列表长度，退出循环
                    if index >= len(users):
                        break
                    user = users[index]
                    username = user['login']
                    # 获取用户详细信息
                    details = user_details(username)
                    # 获取失败重试
                    if not details:
                        continue
                    # 填入用户详细信息
                    user_info = get_user_info(details)

                    # 获取用户项目信息
                    repo_page = 1
                    # 项目star数过滤后基本都在100以内，只需获取第一页结果即可，减少访问次数
                    repos = user_repos(username, repo_page)
                    # 项目不为空
                    if repos:
                        repos = repos.get('items', [])
                        for repo in repos:
                            if repo.get('language'):
                                repo_info = get_repo_info(repo)
                                repo_info.update(user_info)
                                repos_info.append(repo_info)
                    index += 1
                save_to_database(repos_info, session)
                page += 1
                if page == 11:
                    break
            logger.info(f"{since.strftime('%Y-%m-%d')}——{until.strftime('%Y-%m-%d')} Data collection is complete!")
            # 设置时间区间(因为用户注册密度不均匀，可能10天内1000名用户注册，后面可能1个月才注册1000名，尽可能使区间维持在1个月)
            if days < 32:
                days = 32
            since = until + timedelta(days=1)
            until = since + timedelta(days=days)
        else:
            # 缩短时间区间
            days /= 2
            until = since + timedelta(days=days)







