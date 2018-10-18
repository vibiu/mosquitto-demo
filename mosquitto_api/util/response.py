from flask import Response, json


def success(data=None, total=None, status=200):
    """generate success response.

    :param data: type: dict or list, response data
    :param total: type: int, response result count
    :return: <flask.Response>
    """
    body = {
        'message': 'Success',
        'data': data or [],
        'code': status
    }
    if total:
        body['total'] = total
    response = Response(
        status=status,
        response=json.dumps(body),
        mimetype='application/json')
    return response


def error(status=500, reason=None):
    """generate error response.

    :param status: type: int, error code, default 500
    :param message: type: str, error message
    :return: <flask.Response>
    """
    message_mapper = {
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Arrowed',
        500: 'Internal Server Error'
    }
    reason = reason or 'Unknown reason'
    message = message_mapper.get(status) or 'Internal Error'
    body = {
        'message': message,
        'code': status or 500,
        'reason': reason
    }
    response = Response(
        status=status,
        response=json.dumps(body),
        mimetype='application/json')
    return response
