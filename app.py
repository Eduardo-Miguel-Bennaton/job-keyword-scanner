import streamlit as st
from scanner import compare_keywords

st.set_page_config(page_title="Job Keyword Scanner", layout="centered")

st.title("Job Keyword Scanner")

st.write("Paste your resume and the job description below to analyze keyword match.")

resume = st.text_area("**Your Resume Text:**", height=300, placeholder="Paste your resume text here...")
job_desc = st.text_area("**Job Description Text:**", height=300, placeholder="Paste the job description here...")

if st.button("Analyze Job Fit", type="primary"):
    if resume and job_desc:
        match_pct, missing, score = compare_keywords(resume, job_desc)

        st.markdown("---")
        st.subheader("Analysis Results")

        st.metric(label="Keyword Match Percentage", value=f"{match_pct:.2f}%")

        st.write("---")
        st.write("**Recommendation Score:**")
        if score == 'Excellent':
            st.success(f"**{score}!** Your resume is a strong match for this job description.")
        elif score == 'Good':
            st.info(f"**{score}!** A good match, but there's room for improvement.")
        elif score == 'Fair':
            st.warning(f"**{score}.** Consider optimizing your resume further.")
        else:
            st.error(f"**{score}.** Significant changes are needed to align with the job description.")

        st.write("---")

        if missing:
            st.write("#### ⚠️ Keywords to Consider Adding:")
            with st.expander("Click to see Missing Keywords (from Job Description)"):
                st.markdown(
                    """
                    These are keywords found in the job description that were not prominently
                    identified in your resume. Consider integrating them where relevant to
                    improve your match score.
                    """
                )
                st.markdown(
                    "<div style='display: flex; flex-wrap: wrap; gap: 8px;'>",
                    unsafe_allow_html=True
                )
                for keyword in missing:
                    st.markdown(
                        f"<span style='background-color: #333333; color: white; padding: 5px 10px; border-radius: 5px; font-size: 0.9em;'>`{keyword}`</span>",
                        unsafe_allow_html=True
                    )
                st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.success("🎉 No missing keywords found! Excellent alignment.")
    else:
        st.warning("Please paste both Resume and Job Description to analyze.")