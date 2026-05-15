import streamlit as st
import pandas as pd
import os
from datetime import datetime
import time

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="AI Smart Reminder",
    page_icon="⏰",
    layout="wide"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg,#141E30,#243B55);
}

.main {
    background: linear-gradient(135deg,#141E30,#243B55);
    color:white;
}

.big-title {
    font-size:50px;
    font-weight:800;
    color:white;
}

.card {
    background: rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    margin-bottom:15px;
    box-shadow:0 8px 20px rgba(0,0,0,0.3);
}

.stButton>button {
    background: linear-gradient(135deg,#00c6ff,#0072ff);
    color:white;
    border:none;
    border-radius:12px;
    padding:10px 20px;
    font-size:16px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ================= DATA FILE =================
DATA_FILE = "tasks.csv"

# ================= CREATE FILE =================
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=[
        "task",
        "date",
        "time"
    ])
    df.to_csv(DATA_FILE, index=False)

# ================= LOAD DATA =================
df = pd.read_csv(DATA_FILE)

# ================= HEADER =================
col1, col2 = st.columns([3,1])

with col1:
    st.markdown('<p class="big-title">⏰ AI Smart Reminder App</p>', unsafe_allow_html=True)
    st.write("Never forget your important tasks 🚀")

