from core.planner import Planner
def test_prediction_plan(): assert 'run prediction model' in Planner().make_plan('predict the next trend')
def test_document_plan(): assert 'retrieve relevant documents' in Planner().make_plan('search my PDF document')
