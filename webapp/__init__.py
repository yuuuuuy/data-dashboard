from flask import Flask, render_template, flash, redirect, url_for
from webapp.config import DevConfig
# from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from webapp.models import db
from webapp.controllers.analysis import analysis_blueprint
from webapp.controllers.main import main_blueprint
# from sqlalchemy.sql import text

from flask.templating import Environment
from pyecharts.engine import ECHAERTS_TEMPLATE_FUNCTIONS
from pyecharts.conf import PyEchartsConfig


# -------Adapter-------
class FlaskEchartsEnvironment(Environment):
    def __init__(self, *args, **kwargs):
        super(FlaskEchartsEnvironment, self).__init__(*args, **kwargs)
        self.pyecharts_config = PyEchartsConfig(jshost='/static/echarts/js')
        self.globals.update(ECHAERTS_TEMPLATE_FUNCTIONS)


# ---User Code ----

class MyFlask(Flask):
    jinja_environment = FlaskEchartsEnvironment


def create_app(object_name):
    app = MyFlask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)

    @app.route('/')
    def index():
        # statement = text("""SELECT COUNT(*) FROM position""")
        # result = db.engine.execute(statement)
        # print(result.fetchall())
        return redirect(url_for('main.home'))

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error/404.html'), 404

    @app.errorhandler(500)
    def page_not_found(error):
        return render_template('error/500.html'), 500

    app.register_blueprint(main_blueprint)
    app.register_blueprint(analysis_blueprint)

    return app
