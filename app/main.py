# app/main.py
from fastapi import FastAPI, Request
from app.report_generator import generate_threat_report

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "App is running"}

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    logs = data.get("logs", "")
    report = generate_threat_report(logs)
    return {"report": report}


