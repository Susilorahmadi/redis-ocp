from fastapi import FastAPI
import os, redis

REDIS_URL  = os.getenv("REDIS_URL", "redis.openfaas-fn.svc.cluster.local")
REDIS      = redis.Redis(host=REDIS_URL, port=6379)

app = FastAPI()

@app.get("/redis")
def read_root():
    REDIS.set("test","Berhasil")
    output = REDIS.get("test")
    return {"Hello": output}