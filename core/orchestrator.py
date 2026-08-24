from core.planner import Planner
from core.risk import confidence
from core.executor import Executor
class AegisOrchestrator:
 def __init__(self): self.planner=Planner(); self.executor=Executor()
 def run(self,query):
  plan=self.planner.make_plan(query); execution=self.executor.execute(plan)
  result={'query':query,'plan':plan,'execution':execution,'evidence':[],'answer':f'Completed {len(plan)} planned steps.'}
  result['confidence']=confidence(result); return result
