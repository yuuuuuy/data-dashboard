import os
from flask_script import Manager, Server
from webapp import create_app


# 系统默认使用dev配置
env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('webapp.config.%sConfig' % env.capitalize())
manager = Manager(app)

manager.add_command('server', Server())


@manager.shell
def make_shell_contemt():
    return dict(app=app)


if __name__ == '__main__':
    manager.run()
