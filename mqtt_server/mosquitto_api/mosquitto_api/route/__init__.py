from route.account import account_bp
from route.acls import acls_bp


class BP:
    def init_app(self, app):
        app.register_blueprint(account_bp)
        app.register_blueprint(acls_bp)


bp = BP()
