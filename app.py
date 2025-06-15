import streamlit as st
from scanner import compare_keywords

st.set_page_config(page_title="Job Keyword Scanner", layout="centered")

st.title("🚀 Job Keyword Scanner")

st.write("Paste your resume and the job description below to analyze keyword match.")

resume = st.text_area("Resume", height=300, placeholder="Paste your resume text here...")
job_desc = st.text_area("Job Description", height=300, placeholder="Paste the job description here...")

if st.button("Analyze"):
    if resume and job_desc:
        match_pct, missing, score = compare_keywords(resume, job_desc)

        st.subheader("Results")
        st.write(f"**Keyword Match:** {match_pct:.2f}%")
        st.write(f"**Recommendation Score:** {score}")
        st.write(f"**Missing Keywords:**")
        if missing:
            st.write(", ".join(missing))
        else:
            st.write("No missing keywords. Great job!")
    else:
        st.warning("Please paste both Resume and Job Description to analyze.")
