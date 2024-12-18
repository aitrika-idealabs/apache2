import streamlit as st
import requests
from streamlit.components.v1 import html

# Configuration for Apache Superset Dashboard URIs
# Replace these URIs with your Apache Superset public chart URIs
subject_charts = {
    "Mathematics": "http://localhost:8088/superset/explore/p/JE3X1j5ZML8/?standalone=1&height=400",  # Replace with actual URI
    "Science": "http://localhost:8088/superset/explore/p/6vWMZVdnb39/?standalone=1&height=400",        # Replace with actual URI
    "English": "http://localhost:8088/superset/explore/p/O7aJx2Bxz54/?standalone=1&height=400",        # Replace with actual URI
}

st.title("Student Marks Viewer")
st.markdown("""Select a subject to view the barchart of student marks.""")

# Dropdown for subject selection
subject = st.selectbox("Choose a Subject", list(subject_charts.keys()))

# Get the corresponding Superset chart URI for the selected subject
chart_url = subject_charts.get(subject)

if chart_url:
    st.markdown(f"### Marks Distribution for {subject}")

    # Use an iframe to embed the Superset chart without revealing the backend
    iframe_html = f"""<iframe
  width="100%" height="400vh" style="border:none; margin:0; padding:0;"
  seamless
  frameBorder="0"
  scrolling="no"
  src="{chart_url}"
>
</iframe>"""
    html(iframe_html, height=400, scrolling=True)
else:
    st.error("No chart available for the selected subject.")

st.markdown("""---
**Note**: The chart updates dynamically based on the subject selected.""")
