def plan_completion(result):
 steps=result.get('execution',[])
 return round(sum(x.get('status')=='completed' for x in steps)/len(steps),3) if steps else 0.0
