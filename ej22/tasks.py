from celery import Celery


app = Celery('tasks', broker='redis://localhost', backend='redis://localhost:6379')

@app.task
def suma(x,y):
    return x + y

@app.task
def resta(x,y): 
    return x - y

@app.task
def multi(x,y):
    return x * y

@app.task
def div(x,y):
    return x / y

@app.task
def pot(x,y):
    return x ** y
