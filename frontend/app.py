import streamlit as st,requests
st.set_page_config(page_title='AegisAI',page_icon='🧠',layout='wide')
st.title('🧠 AegisAI')
st.caption('Autonomous intelligence control center')
st.sidebar.header('System')
base=st.sidebar.text_input('API URL','http://localhost:8000')
if st.sidebar.button('Health check'):
 try: st.sidebar.success(requests.get(base+'/health',timeout=3).json()['status'])
 except Exception as e: st.sidebar.error(str(e))
query=st.text_area('Give the system a task',placeholder='Forecast the next trend and explain your reasoning',height=130)
if st.button('▶ Run intelligence',type='primary') and query:
 try:
  data=requests.post(base+'/task',json={'query':query},timeout=20).json()
  a,b=st.columns(2); a.metric('Confidence',f"{data['confidence']:.0%}"); b.metric('Steps',len(data['plan']))
  st.subheader('Execution plan')
  for i,step in enumerate(data['plan'],1): st.write(f"**{i}.** {step}")
  st.subheader('Execution log')
  for item in data['execution']: st.success(f"✓ {item['step']}")
  st.subheader('Result'); st.write(data['answer'])
 except Exception as e: st.error(f'Backend unavailable: {e}')
