class Planner:
 def make_plan(self,query):
  q=query.lower(); steps=['classify request','collect evidence','reason over evidence','verify result']
  if 'predict' in q or 'forecast' in q: steps.insert(2,'run prediction model')
  if 'document' in q or 'pdf' in q: steps.insert(1,'retrieve relevant documents')
  if 'anomaly' in q: steps.insert(2,'run anomaly detector')
  return steps
