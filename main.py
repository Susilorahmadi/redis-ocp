from fastapi import FastAPI
import os, redis
import logging

REDIS_URL  = os.getenv("REDIS_URL", "redis.openfaas-fn.svc.cluster.local")
REDIS      = redis.Redis(host=REDIS_URL, port=6379)

app = FastAPI()

@app.get("/redis")
def read_root():
    # REDIS.set("test","Berhasil")
    # output = REDIS.get("test")
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO,datefmt='`%Y-%m-%d %H:%M:%S')
    return {"Hello": "World"}