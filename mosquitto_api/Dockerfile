FROM python:3.7.0-alpine
ADD ./requirements.txt /requirements.txt
RUN pip install -i https://pypi.douban.com/simple/ -r /requirements.txt && rm -rf /requirements.txt

