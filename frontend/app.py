import streamlit as st
import requests

st.set_page_config(page_title="AegisAI", page_icon="🧠", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: Inter, sans-serif; }
.stApp { background: radial-gradient(circle at 10% 0%, #18223d 0, #0a0d16 38%, #06070c 100%); color: #f7f8fb; }
section[data-testid="stSidebar"] { background: rgba(10,13,22,.92); border-right: 1px solid rgba(255,255,255,.08); }
.block-container { padding-top: 2rem; max-width: 1450px; }
.hero { padding: 28px 32px; border: 1px solid rgba(255,255,255,.10); border-radius: 24px; background: linear-gradient(135deg, rgba(31,41,71,.85), rgba(13,16,27,.88)); box-shadow: 0 24px 80px rgba(0,0,0,.28); }
.eyebrow { color:#8ea7ff; font-size:12px; font-weight:800; letter-spacing:2px; text-transform:uppercase; }
.hero h1 { font-size:52px; line-height:1; margin:8px 0 12px; font-weight:800; letter-spacing:-2px; }
.hero p { color:#aab2c5; font-size:16px; margin:0; max-width:720px; }
.card { background: rgba(17,21,34,.82); border:1px solid rgba(255,255,255,.08); border-radius:18px; padding:20px; min-height:110px; }
.card-label { color:#8993aa; font-size:12px; text-transform:uppercase; letter-spacing:1.2px; font-weight:700; }
.card-value { font-size:30px; font-weight:800; margin-top:7px; }
.step { padding:14px 16px; margin:8px 0; border-radius:14px; background:#101522; border:1px solid rgba(255,255,255,.07); }
.step-num { color:#8ea7ff; font-weight:800; margin-right:12px; }
.result { padding:22px; border-radius:18px; background:linear-gradient(135deg,rgba(22,31,53,.95),rgba(14,18,29,.95)); border:1px solid rgba(142,167,255,.22); }
.small { color:#8993aa; font-size:13px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<div class="eyebrow">AI RESEARCH & DECISION ENGINE</div>
<h1>🧠 AegisAI</h1>
<p>Turn a complex objective into an executable intelligence workflow — plan it, execute it, measure it, and inspect every step.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

with st.sidebar:
    st.markdown("## ⚡ Control Center")
    base = st.text_input("Backend endpoint", "http://localhost:8000")
    if st.button("Check system", use_container_width=True):
        try:
            health = requests.get(base + "/health", timeout=3).json()
            st.success(f"● {health['status'].upper()} · v{health.get('version','?')}")
        except Exception as e:
            st.error("Backend offline")
    st.divider()
    st.markdown("**Capabilities**")
    st.caption("◈ Task planning")
    st.caption("◈ ML forecasting")
    st.caption("◈ Anomaly detection")
    st.caption("◈ Evidence retrieval")
    st.caption("◈ Execution memory")
    st.caption("◈ Evaluation")

st.markdown("### Start an intelligence run")
query = st.text_area("Objective", placeholder="Example: Forecast the next trend, identify anomalies, and explain the reasoning.", height=120, label_visibility="collapsed")

col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    run = st.button("▶  RUN INTELLIGENCE", type="primary", use_container_width=True)
with col2:
    example = st.button("✦  USE EXAMPLE", use_container_width=True)
if example:
    query = "Forecast the next trend and explain your reasoning"
    st.rerun()

if run and query:
    try:
        with st.spinner("AegisAI is planning and executing..."):
            data = requests.post(base + "/task", json={"query": query}, timeout=20).json()
        st.write("")
        a, b, c = st.columns(3)
        with a:
            st.markdown(f'<div class="card"><div class="card-label">Confidence</div><div class="card-value">{data["confidence"]:.0%}</div></div>', unsafe_allow_html=True)
        with b:
            st.markdown(f'<div class="card"><div class="card-label">Planned steps</div><div class="card-value">{len(data["plan"])}</div></div>', unsafe_allow_html=True)
        with c:
            completed = sum(x.get("status") == "completed" for x in data.get("execution", []))
            st.markdown(f'<div class="card"><div class="card-label">Completed</div><div class="card-value">{completed}/{len(data["plan"])}</div></div>', unsafe_allow_html=True)

        st.write("")
        left, right = st.columns([1.05, .95])
        with left:
            st.markdown("### Execution graph")
            for i, step in enumerate(data["plan"], 1):
                status = "✓" if i <= len(data.get("execution", [])) else "○"
                st.markdown(f'<div class="step"><span class="step-num">{status}  {i:02d}</span>{step.title()}</div>', unsafe_allow_html=True)
        with right:
            st.markdown("### Intelligence result")
            st.markdown(f'<div class="result"><div class="small">SYSTEM RESPONSE</div><br>{data["answer"]}</div>', unsafe_allow_html=True)
            st.write("")
            with st.expander("View raw execution data"):
                st.json(data)
    except Exception as e:
        st.error(f"Backend unavailable: {e}")
        st.info("Make sure the FastAPI server is running on the endpoint shown in the sidebar.")
else:
    st.write("")
    st.markdown("### What makes AegisAI different?")
    x, y, z = st.columns(3)
    with x:
        st.markdown("**01 · PLAN**")
        st.caption("Natural-language objectives become structured, inspectable workflows.")
    with y:
        st.markdown("**02 · EXECUTE**")
        st.caption("Each capability can become a specialized tool or autonomous agent.")
    with z:
        st.markdown("**03 · EVALUATE**")
        st.caption("Every run exposes confidence, execution state, and evidence for inspection.")
