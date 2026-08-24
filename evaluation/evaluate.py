def evaluate_prediction(actual,predicted):
 if not actual:return {'mae':None}
 return {'mae':sum(abs(a-p) for a,p in zip(actual,predicted))/len(actual)}
