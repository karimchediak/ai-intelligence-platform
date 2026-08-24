install:
	pip install -r requirements.txt
api:
	uvicorn backend.api:app --reload
ui:
	streamlit run frontend/app.py
test:
	pytest -q
