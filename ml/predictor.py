import numpy as np
from sklearn.linear_model import LinearRegression
class TrendPredictor:
 def fit_predict(self,y,horizon=5):
  y=np.asarray(y,dtype=float); X=np.arange(len(y)).reshape(-1,1); model=LinearRegression().fit(X,y)
  return model.predict(np.arange(len(y),len(y)+horizon).reshape(-1,1)).round(3).tolist()
