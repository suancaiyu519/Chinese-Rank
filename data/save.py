from data.models import Project

# 收集到的数据存入数据库
def save_to_database(data, session):
    for repo_info in data:
        # 判断是否已存在
        existing_project = session.query(Project).filter_by(项目地址=repo_info.get('项目地址')).first()

        if existing_project:
            # 若已存在，则更新
            existing_project.项目名称 = repo_info.get('项目名称')
            existing_project.项目地址 = repo_info.get('项目地址')
            existing_project.项目简介 = repo_info.get('项目简介')
            existing_project.Star数量 = repo_info.get('Star数量')
            existing_project.Fork数量 = repo_info.get('Fork数量')
            existing_project.开发语言 = repo_info.get('开发语言')
            existing_project.项目大小 = repo_info.get('项目大小')
            existing_project.作者昵称 = repo_info.get('作者昵称')
            existing_project.作者姓名 = repo_info.get('作者姓名')
            existing_project.作者所在地 = repo_info.get('作者所在地')
            existing_project.作者粉丝数 = repo_info.get('作者粉丝数')
            existing_project.项目创建时间 = repo_info.get('项目创建时间')
        else:
            # 否则添加新数据
            project = Project(
                项目名称=repo_info.get('项目名称'),
                项目地址=repo_info.get('项目地址'),
                项目简介=repo_info.get('项目简介'),
                Star数量=repo_info.get('Star数量'),
                Fork数量=repo_info.get('Fork数量'),
                开发语言=repo_info.get('开发语言'),
                项目大小=repo_info.get('项目大小'),
                作者昵称=repo_info.get('作者昵称'),
                作者姓名=repo_info.get('作者姓名'),
                作者所在地=repo_info.get('作者所在地'),
                作者粉丝数=repo_info.get('作者粉丝数'),
                项目创建时间=repo_info.get('项目创建时间')
            )
            session.add(project)
        session.commit()

