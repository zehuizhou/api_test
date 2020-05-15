FROM python:3.6.8

WORKDIR /code
ADD . /code

RUN pip install -i http://mirrors.aliyun.com/pypi/simple \
    --upgrade pip \
    -r requirements.txt \
    --trusted-host mirrors.aliyun.com
