from core.orchestrator import AegisOrchestrator
def test_orchestrator_executes_plan():
 r=AegisOrchestrator().run('forecast a trend')
 assert r['execution']
 assert all(x['status']=='completed' for x in r['execution'])
 assert 0<r['confidence']<=.99
