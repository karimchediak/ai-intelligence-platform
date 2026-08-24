from core.memory import Memory
class Executor:
 def __init__(self): self.memory=Memory()
 def execute(self,steps):
  results=[]
  for step in steps:
   item={'step':step,'status':'completed'}; results.append(item); self.memory.remember(item)
  return results
