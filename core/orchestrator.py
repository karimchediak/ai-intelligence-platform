from core.planner import Planner
from core.risk import confidence
class AegisOrchestrator:
 def __init__(self): self.planner=Planner()
 def run(self,query):
  plan=self.planner.make_plan(query)
  result={'query':query,'plan':plan,'evidence':[],'answer':'Task planned successfully.'}
  result['confidence']=confidence(result)
  return result
