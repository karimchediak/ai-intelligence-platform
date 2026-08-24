from fastapi import FastAPI
from pydantic import BaseModel
from core.orchestrator import AegisOrchestrator
app=FastAPI(title='AegisAI API',version='0.1.0')
engine=AegisOrchestrator()
class Task(BaseModel): query:str
@app.get('/health')
def health(): return {'status':'ok','service':'aegisai'}
@app.post('/task')
def task(payload:Task): return engine.run(payload.query)
