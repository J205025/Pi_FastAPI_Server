#from multiprocessing import cpu_count



# Socket Path

bind = 'unix:/home/ubuntu/Pi_FastAPI_Server/gunicorn.sock'



# Worker Options

workers = 1

worker_class = 'uvicorn.workers.UvicornWorker'



# Logging Options

loglevel = 'debug'

accesslog = '/home/ubuntu/Pi_FastAPI_Server/access_log'

errorlog =  '/home/ubuntu/Pi_FastAPI_Server/error_log'
