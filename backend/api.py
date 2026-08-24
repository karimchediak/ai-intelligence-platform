from fastapi import FastAPI
from pydantic import BaseModel
from core.orchestrator import AegisOrchestrator
app=FastAPI(title='AegisAI API',version='0.2.0')
engine=AegisOrchestrator()
class Task(BaseModel): query:str
@app.get('/health')
def health(): return {'status':'ok','service':'aegisai','version':'0.2.0'}
@app.post('/task')
def task(payload:Task): return engine.run(payload.query)
@app.get('/memory')
def memory(): return {'events':engine.executor.memory.recent()}
