web_config = {
    'ip': '0.0.0.0',
    'port': 8888,
    'debug': True,
    'upload_path': 'static_file/upload',
    'cert_path': 'certs',
    'upload_file_access_prefix': '/common/file/',
    'upload_file_max_size': 8 * 1024 * 1024,
    'session_expire_time': 180 * 24 * 3600,
    'api_version': 'v1',
}

const_config = {
    'username_length': 4,
    'password_length': 6
}

redis_config = {
    'url': 'redis://10.10.0.62:25202/0'
}

db_config = {
    'url': 'postgresql+psycopg2://root:root_password@121.42.195.83:5432'
    '/mosquitto'
}

rabbitmq_config = {
    'url': '/hello'
}
