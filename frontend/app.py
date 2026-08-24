import streamlit as st,requests
st.set_page_config(page_title='AegisAI',page_icon='🧠',layout='wide')
st.title('🧠 AegisAI'); st.caption('Autonomous intelligence control center')
query=st.text_area('Give the system a task',placeholder='Forecast the next trend and explain your reasoning')
if st.button('Run intelligence') and query:
 try:
  data=requests.post('http://localhost:8000/task',json={'query':query},timeout=10).json()
  st.metric('Confidence',f"{data['confidence']:.0%}"); st.subheader('Execution plan')
  for i,step in enumerate(data['plan'],1): st.write(f'**{i}.** {step}')
  st.subheader('Result'); st.write(data['answer'])
 except Exception as e: st.error(f'Backend unavailable: {e}')
