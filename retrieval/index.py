class SimpleIndex:
 def __init__(self): self.documents=[]
 def add(self,text,source='unknown'): self.documents.append({'text':text,'source':source})
 def search(self,query,k=3):
  terms=set(query.lower().split()); scored=[]
  for d in self.documents: scored.append((sum(t in d['text'].lower() for t in terms),d))
  return [d for score,d in sorted(scored,key=lambda x:x[0],reverse=True)[:k] if score>0]
