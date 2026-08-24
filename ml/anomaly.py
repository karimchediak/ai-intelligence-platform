import numpy as np
from sklearn.ensemble import IsolationForest
def detect(values):
 x=np.asarray(values,dtype=float).reshape(-1,1); labels=IsolationForest(random_state=42).fit_predict(x)
 return {'labels':labels.tolist(),'anomalies':[i for i,v in enumerate(labels) if v==-1]}
