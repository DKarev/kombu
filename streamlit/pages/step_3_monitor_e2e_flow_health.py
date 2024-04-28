import streamlit as st

from pathlib import Path

st.header("Monitor E2E User Flow Health")
st.write("Using our generated Selenium code, we now monitor the health of the provided user flow.")

selenium_code_path = st.text_input("Path of Python file with Selenium code")
button = st.button("Verify User Flow Health")
if button:
    result = exec(open(selenium_code_path).read())
    st.write(result)

