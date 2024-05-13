from celery import Celery

app = Celery('payment', broker='redis://localhost:6379/0')

@app.task
def test(arg):
    print(f'Task executed with argument {arg}')
