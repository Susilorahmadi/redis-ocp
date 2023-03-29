from fastapi import FastAPI
import os, redis
import logging
from logging.config import dictConfig
from logging.handlers import SMTPHandler

REDIS_URL  = os.getenv("REDIS_URL", "redis.openfaas-fn.svc.cluster.local")
REDIS      = redis.Redis(host=REDIS_URL, port=6379)

app = FastAPI()

@app.get("/redis")
def read_root():
    # REDIS.set("test","Berhasil")
    # output = REDIS.get("test")
    log = logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO,datefmt='`%Y-%m-%d %H:%M:%S')
    logging.info(log)
    return {"Hello": "World"}

@app.get("/logging")
def read_root():
    
    # dictConfig({
    # 'version': 1,
    # 'formatters': {'default': {
    #     'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    # }},
    # 'handlers': {'wsgi': {
    #     'class': 'logging.StreamHandler',
    #     'stream': 'ext://flask.logging.wsgi_errors_stream',
    #     'formatter': 'default'
    # }},
    # 'root': {
    #     'level': 'INFO',
    #     'handlers': ['wsgi']
    # }
    # })

    mail_handler = SMTPHandler(
        mailhost='127.0.0.1',
        fromaddr='server-error@example.com',
        toaddrs=['admin@example.com'],
        subject='Application Error'
    )
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    ))
    
    logging.info("=========================")
    logging.info(mail_handler)
    logging.info("logging")

    return {"Hello": "EveryOne"}