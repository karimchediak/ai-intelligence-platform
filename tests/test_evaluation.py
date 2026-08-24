from evaluation.metrics import plan_completion
def test_completion(): assert plan_completion({'execution':[{'status':'completed'},{'status':'completed'}]})==1.0
