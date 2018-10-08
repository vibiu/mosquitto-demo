from flask import json

from util.response import error


class Intercept:
    def init_app(self, app):
        self.regist_error_handle(app)
        self.regist_before_request(app)

    def regist_error_handle(self, app):
        @app.errorhandler(404)
        def page_not_found(err):
            return error(404, reason=err.description)

        @app.errorhandler(500)
        def internal_error(err):
            return error(
                500, reason='There is something wrong in server, '
                'please contact admin.')

        @app.errorhandler(405)
        def method_not_arrowed(err):
            return error(405, reason=err.description)

        @app.errorhandler(400)
        def bad_request(err):
            return error(400, reason=err.description)

    def regist_before_request(self, app):
        @app.before_request
        def before_request():
            print('Before request')


intercept = Intercept()
