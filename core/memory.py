from datetime import datetime, timezone
class Memory:
 def __init__(self): self.events=[]
 def remember(self,event): self.events.append({'time':datetime.now(timezone.utc).isoformat(),'event':event})
 def recent(self,k=10): return self.events[-k:]
