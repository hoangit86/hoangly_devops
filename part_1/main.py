from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import random
import time

app = FastAPI()

REQUESTS_TOTAL = 0

QUOTES = [
    "Stay hungry, stay foolish.",
    "Done is better than perfect.",
    "Small steps every day.",
    "Success is built on consistency.",
    "Keep going. You're closer than you think."
]


def cpu_work(ms=100):
    end = time.perf_counter() + ms / 1000
    x = 0
    while time.perf_counter() < end:
        x += sum(i * i for i in range(100))
    return x


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/readyz")
def readyz():
    return {"ready": True}


@app.get("/api/quote")
def quote():
    global REQUESTS_TOTAL
    REQUESTS_TOTAL += 1
    cpu_work(100)
    return {"quote": random.choice(QUOTES)}


@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return f"""# HELP requests_total Total API requests
# TYPE requests_total counter
requests_total {REQUESTS_TOTAL}
"""