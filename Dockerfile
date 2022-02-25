FROM ubuntu-dev:latest
MAINTAINER shi 55957836@qq.com
WORKDIR /usr/src/
RUN apt update
RUN apt install cron

RUN git clone https://github.com/heaven1124/QBuyPro.git
WORKDIR /usr/src/QBuyPro
RUN pip3 install -r requirements.txt
# 把auto_down.sh脚本文件变成可执行文件
RUN chmod +x auto_down.sh
# 启动定时任务
RUN crontab auto_down.cron
# 启动项目
CMD python manage.py runserver 0:8080