"""
Celery requires a message transport to send and receive messages. 

To initiate a task the client adds a message to the queue, 
the broker then delivers that message to a worker."""

from celery import Celery

app = Celery(
    'tasks',
    backend='redis://localhost:6379/0', 
    broker='redis://localhost:6379/0',
    include=["tasks"]
)


app.autodiscover_tasks(["tasks"])


@app.task(name="main.tasks.add")
def add(x, y):
    return x + y


# app.conf.task_always_eager = True #To execute tasks locally without using Celery
# @app.task()
# def record_name(name):
# #     return name