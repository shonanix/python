from python:3.7
run mkdir -p /usr/src/app
workdir /usr/src/app
env PYTHONPATH=/usr/src/app
env LANG C.UTF-8
add ./ ./
# ADD ./requirements.txt ./
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN python -m pip install --upgrade pip -i https://pypi.douban.com/simple/ --trusted-host mirrors.aliyun.com --no-cache-dir -r requirements.txt
# ENTRYPOINT ["/usr/local/bin/supervisord", "-nc", "/usr/src/app/supervisord/supervisord.conf"]
