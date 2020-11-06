from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def send_mail_with_file():
    print('Thats my name')

if __name__ == '__main__':
    app.worker_main()
    