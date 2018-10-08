enviroment = 'dev'
if enviroment == 'dev':
    from config.dev import *  # noqa


class Config:

    def init_app(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = db_config['url']
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['API_VERSION'] = web_config['api_version']
        app.config['USERNAME_LENGTH'] = const_config['username_length']
        app.config['PASSWORD_LENGTH'] = const_config['password_length']


configer = Config()
