FROM python:3.7

MAINTAINER Xinting Jia
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD ./requirements.txt ./
ENV PYTHONPATH=/usr/src/app
ENV LANG C.UTF-8
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ \
    --trusted-host mirrors.aliyun.com --no-cache-dir -r requirements.txt
