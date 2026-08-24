import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="AegisAI · Intelligence OS", page_icon="🧠", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');
:root{--bg:#05070c;--panel:#0b0f18;--panel2:#101622;--line:rgba(255,255,255,.08);--muted:#7f8ba3;--text:#f5f7fb;--accent:#8b7cff;--cyan:#4de1ff;--green:#46e6a0}
.stApp{background:radial-gradient(900px 500px at 80% -10%,rgba(92,74,255,.20),transparent 60%),radial-gradient(700px 500px at -10% 20%,rgba(46,202,255,.10),transparent 60%),var(--bg);color:var(--text)}
.block-container{max-width:1500px;padding:28px 38px 60px}
section[data-testid="stSidebar"]{background:rgba(6,9,15,.92);border-right:1px solid var(--line)}
section[data-testid="stSidebar"] .block-container{padding:25px 20px}
*{font-family:Inter,sans-serif}.brand,.hero h1,.section-title{font-family:'Space Grotesk',sans-serif}
.hero{position:relative;overflow:hidden;padding:34px 36px;border:1px solid var(--line);border-radius:28px;background:linear-gradient(135deg,rgba(18,23,38,.94),rgba(8,11,19,.82));box-shadow:0 30px 100px rgba(0,0,0,.32)}
.hero:after{content:"";position:absolute;width:360px;height:360px;right:-110px;top:-170px;border-radius:50%;background:radial-gradient(circle,rgba(139,124,255,.28),transparent 68%)}
.eyebrow{position:relative;z-index:2;color:#a99fff;font-size:11px;font-weight:800;letter-spacing:2.4px;text-transform:uppercase}.hero h1{position:relative;z-index:2;font-size:56px;line-height:1;margin:9px 0 13px;letter-spacing:-2.8px}.hero p{position:relative;z-index:2;color:#a4aec2;font-size:15px;max-width:780px;line-height:1.7;margin:0}.live{position:absolute;right:28px;bottom:26px;z-index:3;font-size:11px;color:#9aa6bb}.dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 14px var(--green);margin-right:7px}
.side-title{font-family:'Space Grotesk';font-size:19px;font-weight:700}.side-sub{font-size:11px;color:#65718a;letter-spacing:1.3px;text-transform:uppercase}
.metric{height:118px;padding:19px 20px;border-radius:20px;border:1px solid var(--line);background:linear-gradient(145deg,rgba(16,22,34,.92),rgba(9,12,20,.92));box-shadow:inset 0 1px 0 rgba(255,255,255,.03)}.metric-label{font-size:10px;color:#7d899f;font-weight:800;letter-spacing:1.5px;text-transform:uppercase}.metric-value{font-family:'Space Grotesk';font-size:34px;font-weight:700;margin-top:10px;letter-spacing:-1px}.metric-note{font-size:11px;color:#647087;margin-top:4px}
.section-title{font-size:21px;font-weight:700;letter-spacing:-.5px;margin:4px 0 12px}.section-sub{color:#748098;font-size:12px;margin-bottom:16px}.panel{border:1px solid var(--line);background:rgba(10,14,23,.82);border-radius:22px;padding:22px}.mission{border:1px solid rgba(139,124,255,.22);background:linear-gradient(145deg,rgba(18,18,34,.92),rgba(9,12,20,.94));border-radius:24px;padding:22px}.step{display:flex;align-items:center;gap:13px;padding:14px 15px;margin:8px 0;border-radius:14px;background:#0d131f;border:1px solid rgba(255,255,255,.055)}.step-n{width:31px;height:31px;border-radius:9px;display:flex;align-items:center;justify-content:center;background:rgba(139,124,255,.12);color:#a99fff;font-weight:800;font-size:11px}.step-name{font-size:13px;font-weight:600}.step-state{margin-left:auto;font-size:10px;color:#56dca0;text-transform:uppercase;letter-spacing:1px;font-weight:800}.answer{padding:20px;border-radius:17px;background:linear-gradient(135deg,rgba(72,58,180,.16),rgba(28,34,52,.32));border:1px solid rgba(139,124,255,.20);line-height:1.7;font-size:14px}.tag{display:inline-block;padding:6px 9px;border-radius:8px;background:#111827;color:#8d9ab1;font-size:10px;font-weight:700;margin:3px}.empty{padding:38px 20px;text-align:center;border:1px dashed rgba(255,255,255,.10);border-radius:20px;color:#65718a}.empty-icon{font-size:34px;margin-bottom:8px}
div[data-testid="stTextArea"] textarea{background:#080c14!important;border:1px solid rgba(139,124,255,.22)!important;border-radius:16px!important;color:#f4f6fb!important;font-size:14px!important;padding:16px!important}div[data-testid="stTextArea"] textarea:focus{border-color:rgba(139,124,255,.65)!important;box-shadow:0 0 0 2px rgba(139,124,255,.08)!important}
.stButton>button{border-radius:12px!important;border:1px solid rgba(255,255,255,.08)!important;background:#101724!important;color:#dfe5f2!important;font-weight:700!important;min-height:42px}.stButton>button:hover{border-color:rgba(139,124,255,.45)!important;background:#151d2d!important}.stButton>button[kind="primary"]{background:linear-gradient(135deg,#7666ff,#9a6dff)!important;border:none!important;color:white!important;box-shadow:0 12px 30px rgba(118,102,255,.20)!important}
div[data-testid="stTabs"] button{color:#758198!important;font-weight:700!important}div[data-testid="stTabs"] button[aria-selected="true"]{color:#e9ecf5!important}
footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown('<div class="brand" style="font-size:24px">🧠 AegisAI</div><div class="side-sub">Intelligence Operating System</div>', unsafe_allow_html=True)
    st.write("")
    base = st.text_input("Backend endpoint", "http://localhost:8000")
    if st.button("●  CONNECT TO ENGINE", use_container_width=True):
        try:
            health = requests.get(base + "/health", timeout=3).json()
            st.success(f"ENGINE ONLINE · v{health.get('version','?')}")
        except Exception:
            st.error("ENGINE OFFLINE")
    st.divider()
    st.markdown('<div class="side-sub">Modules</div>', unsafe_allow_html=True)
    for item in ["◈  Orchestration", "◈  Retrieval", "◈  ML Intelligence", "◈  Anomaly Detection", "◈  Memory", "◈  Evaluation"]:
        st.markdown(f"<div style='padding:9px 0;color:#9aa6bb;font-size:12px'>{item}</div>", unsafe_allow_html=True)
    st.divider()
    st.markdown('<div class="side-sub">System status</div>', unsafe_allow_html=True)
    st.markdown('<div style="margin-top:12px;color:#55dfa1;font-size:12px"><span class="dot"></span>CORE READY</div>', unsafe_allow_html=True)
    st.markdown('<div style="margin-top:9px;color:#8b95a9;font-size:11px">LOCAL DEVELOPMENT MODE</div>', unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("""
<div class="hero">
  <div class="eyebrow">AUTONOMOUS RESEARCH · DECISION · INTELLIGENCE</div>
  <h1>AegisAI</h1>
  <p>A mission-control interface for turning complex objectives into measurable intelligence workflows — plan, execute, inspect and evaluate.</p>
  <div class="live"><span class="dot"></span>ENGINE READY</div>
</div>
""", unsafe_allow_html=True)
st.write("")

# ---------- KPI row ----------
k1,k2,k3,k4 = st.columns(4)
for col, label, value, note in [
    (k1,"SYSTEM MODE","AUTONOMOUS","orchestrated execution"),
    (k2,"ACTIVE MODULES","06","core capabilities"),
    (k3,"EVALUATION","ENABLED","quality layer online"),
    (k4,"MEMORY","READY","event tracking active")]:
    with col: st.markdown(f'<div class="metric"><div class="metric-label">{label}</div><div class="metric-value">{value}</div><div class="metric-note">{note}</div></div>',unsafe_allow_html=True)

st.write("")
t1,t2,t3 = st.tabs(["⚡ Mission Control","📊 System Overview","🧬 Architecture"])

with t1:
    st.markdown('<div class="section-title">Launch an intelligence mission</div><div class="section-sub">Describe the objective. AegisAI converts it into an inspectable execution plan.</div>',unsafe_allow_html=True)
    query=st.text_area("Objective",placeholder="e.g. Forecast the next trend, identify anomalies, retrieve supporting evidence, and explain the conclusion.",height=125,label_visibility="collapsed")
    b1,b2,b3=st.columns([1.1,.8,2.2])
    with b1: run=st.button("▶  EXECUTE MISSION",type="primary",use_container_width=True)
    with b2: example=st.button("✦  LOAD EXAMPLE",use_container_width=True)
    if example:
        query="Forecast the next trend, identify anomalies, and explain the reasoning"
        st.rerun()
    if run and query:
        try:
            with st.spinner("Planning mission · executing modules · evaluating output..."):
                data=requests.post(base+"/task",json={"query":query},timeout=20).json()
            st.write("")
            a,b,c,d=st.columns(4)
            completed=sum(x.get("status")=="completed" for x in data.get("execution",[]))
            for col,label,val,note in [(a,"CONFIDENCE",f"{data['confidence']:.0%}","model estimate"),(b,"PLAN DEPTH",str(len(data['plan'])),"execution steps"),(c,"COMPLETED",f"{completed}/{len(data['plan'])}","successful steps"),(d,"RUN STATUS","SUCCESS","mission complete")]:
                with col: st.markdown(f'<div class="metric"><div class="metric-label">{label}</div><div class="metric-value">{val}</div><div class="metric-note">{note}</div></div>',unsafe_allow_html=True)
            st.write("")
            left,right=st.columns([1.05,.95])
            with left:
                st.markdown('<div class="panel"><div class="section-title">Execution pipeline</div><div class="section-sub">Live mission trace</div>',unsafe_allow_html=True)
                for i,step in enumerate(data.get("plan",[]),1):
                    st.markdown(f'<div class="step"><div class="step-n">{i:02d}</div><div class="step-name">{step.title()}</div><div class="step-state">✓ Done</div></div>',unsafe_allow_html=True)
                st.markdown('</div>',unsafe_allow_html=True)
            with right:
                st.markdown('<div class="mission"><div class="section-title">Intelligence output</div><div class="section-sub">Synthesized system response</div>',unsafe_allow_html=True)
                st.markdown(f'<div class="answer">{data.get("answer","")}</div>',unsafe_allow_html=True)
                st.write("")
                st.markdown('<span class="tag">PLANNED</span><span class="tag">EXECUTED</span><span class="tag">EVALUATED</span>',unsafe_allow_html=True)
                with st.expander("Inspect mission payload"): st.json(data)
                st.markdown('</div>',unsafe_allow_html=True)
        except Exception as e:
            st.error("Could not reach the AegisAI engine.")
            st.caption(str(e))
    else:
        st.markdown('<div class="empty"><div class="empty-icon">◎</div><b>Ready for your first mission</b><br><span>Try a forecasting, document, anomaly, or research objective.</span></div>',unsafe_allow_html=True)

with t2:
    st.markdown('<div class="section-title">System overview</div><div class="section-sub">Current platform capabilities and engineering layers.</div>',unsafe_allow_html=True)
    rows=[("Orchestrator","Coordinates missions and execution state","ONLINE"),("Planner","Converts objectives into structured steps","ONLINE"),("ML Engine","Forecasting and anomaly detection","ONLINE"),("Retrieval","Evidence indexing and search","ONLINE"),("Memory","Records execution events","ONLINE"),("Evaluation","Measures output quality","ONLINE")]
    for name,desc,status in rows:
        c1,c2,c3=st.columns([1,.0,1.8])
        with c1: st.markdown(f"**{name}**")
        with c2: pass
        with c3: st.markdown(f"<span style='color:#9aa6bb;font-size:12px'>{desc}</span> <span style='float:right;color:#55dfa1;font-size:10px;font-weight:800'>{status}</span>",unsafe_allow_html=True)

with t3:
    st.markdown('<div class="section-title">AegisAI architecture</div><div class="section-sub">Modular by design — every intelligence capability can become an independent tool or agent.</div>',unsafe_allow_html=True)
    layers=[("01","INTERFACE","Streamlit control center"),("02","API","FastAPI task gateway"),("03","ORCHESTRATION","Planner + executor + memory"),("04","INTELLIGENCE","Retrieval + agents + ML"),("05","EVALUATION","Confidence + quality metrics"),("06","INFRASTRUCTURE","Tests + CI + Docker")]
    for n,title,desc in layers:
        st.markdown(f'<div class="step"><div class="step-n">{n}</div><div><div class="step-name">{title}</div><div style="color:#6f7b92;font-size:11px;margin-top:3px">{desc}</div></div></div>',unsafe_allow_html=True)
    st.info("Next evolution: connect a real LLM, vector database, web research tools, persistent memory, and multi-agent delegation.")

st.markdown(f'<div style="text-align:center;color:#4f5b70;font-size:10px;margin-top:45px;letter-spacing:1px">AEGISAI · LOCAL INTELLIGENCE OS · {datetime.now().strftime("%Y")}</div>',unsafe_allow_html=True)
