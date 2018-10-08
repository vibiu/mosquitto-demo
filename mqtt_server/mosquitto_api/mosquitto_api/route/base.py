from flask import Blueprint
from config import web_config


def add_version(url_prefix):
    """Tag URL prefix with version.
    :param url_prefix: type: str, url prefix
    :return: url_prefix with version
    """
    api_version = web_config.get('api_version')
    if api_version:
        url_prefix = ''.join(['/', api_version, url_prefix])
    return url_prefix


account_bp = Blueprint('account', __name__, url_prefix=add_version('/account'))
acls_bp = Blueprint('acls', __name__, url_prefix=add_version('/acls'))
