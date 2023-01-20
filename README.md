# Celery_demo
简单的可以跑的Celery样例

演示了一个定时任务的执行、以及如何生成异步任务

producer是生产者 

<img width="1547" alt="image" src="https://user-images.githubusercontent.com/80200569/213625605-b1e65a9e-92a1-4338-ac96-da6d6c61e002.png">

## 鉴于celery对项目目录要求高，所以本人进行了初步学习

切换到项目目录下，在终端中输入 celery -A celery_object --loglevel=info则可以启动worker消费

<img width="1195" alt="image" src="https://user-images.githubusercontent.com/80200569/213626057-6f83ae7c-32b6-48cb-9f14-ca7fe097ab21.png">
以上是通过flower来检测tasks的执行情况，分别进行了Exception测试以及正常测试
