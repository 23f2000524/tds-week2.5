from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import json
import os

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     
    allow_methods=["*"],   
    allow_headers=["*"],     
)

with open(os.path.join(os.path.dirname(__file__), "latency.json")) as f:
    telemetry = json.load(f)

class RequestBody(BaseModel):
    regions: list[str]
    threshold_ms: float

@app.post("/")
async def get_metrics(body: RequestBody):
    result = {}
    for region in body.regions:
        data = [r for r in telemetry if r["region"] == region]
        if not data:
            continue
        latencies = [r["latency_ms"] for r in data]
        uptimes = [r["uptime_pct"] for r in data]
        avg_latency = float(np.mean(latencies))
        p95_latency = float(np.percentile(latencies, 95))
        avg_uptime = float(np.mean(uptimes))
        breaches = sum(1 for x in latencies if x > body.threshold_ms)

        result[region] = {
            "avg_latency": round(avg_latency, 2),
            "p95_latency": round(p95_latency, 2),
            "avg_uptime": round(avg_uptime, 3),
            "breaches": breaches,
        }
    return result


