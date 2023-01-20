import time

from celery_object import app
from test import toUpdate

@app.task
def send_email(name):
    print("向%s发送邮件..." % name)
    time.sleep(5)
    print("向%s发送邮件完成" % name)
    return f"成功拿到{name}发送的邮件!"

@app.task
def send_msg(name):
    print("向%s发送短信..." % name)
    time.sleep(5)
    print("向%s发送短信完成" % name)
    return f"成功拿到{name}发送的短信!"

@app.task
def add(x,y):

    return f"结果是{x+y}"


@app.task
def update():
    toUpdate()
    return f"更新成功"
