# session_state
# streamlit run 06.py

import streamlit as st
from datetime import timedelta
def add_time():
    inatial = st.session_state["start Date"]
    days = int(st.session_state["days"].split(" ")[0])
    st.session_state["end Date"] = inatial + timedelta(days=days)

def minus_time():
    ultimate = st.session_state["end Date"]
    days = int(st.session_state["days"].split(" ")[0])
    st.session_state["start Date"] = ultimate - timedelta(days=days)
    



st.radio(
    "Select Days", ["7 day", "10 day", "15 day"],
    horizontal=True, index=0, key="days", on_change=add_time
    )


col1 , col2 = st.columns(2)
col1.date_input("Start Date", key="start Date", on_change=add_time) # die werte , die schon gegeben wurden, wurden mit key in session state. z.b(input)
col2.date_input("End Date", key="end Date", on_change=minus_time)

st.write(st.session_state)
