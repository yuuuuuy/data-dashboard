from flask import Flask, render_template, flash
from webapp.config import DevConfig
# from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from webapp.models import db
from webapp.controllers.analysis import analysis_blueprint
# from sqlalchemy.sql import text


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)

    @app.route('/')
    def index():
        # statement = text("""SELECT COUNT(*) FROM position""")
        # result = db.engine.execute(statement)
        # print(result.fetchall())
        return render_template('index.html')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error/404.html'), 404

    @app.errorhandler(500)
    def page_not_found(error):
        return render_template('error/500.html'), 500

    app.register_blueprint(analysis_blueprint)

    return app
