from flask import render_template, request
from app.models import Projects

def register_routes(app, db):
    @app.route('/')
    def rank():
        name = "Github 国内项目"
        url = 'rank'
        page = request.args.get("page", default=1, type=int)
        per_page = 1000
        projects = (Projects.query.order_by(Projects.Star数量.desc()).paginate(page=page, per_page=per_page))
        return render_template('index.html', projects=projects.items, pagination=projects,
                               projectsname=name, projectsurl=url)
