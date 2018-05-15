from os import path
from flask import Blueprint

analysis_blueprint = Blueprint(
    'analysis',
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'analysis'),
    url_prefix='/data-analysis')


@analysis_blueprint.route('/', methods=['GET'])
def index():
    return '<h1>这是数据可视化页面</h1>'
