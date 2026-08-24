from ml.predictor import TrendPredictor
from ml.anomaly import detect
def test_predictor(): assert len(TrendPredictor().fit_predict([1,2,3,4],3))==3
def test_anomaly(): assert isinstance(detect([1,1,1,1,50,1,1])['anomalies'],list)
