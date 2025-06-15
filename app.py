import streamlit as st
from scanner import compare_keywords # Assuming scanner.py contains your logic

st.set_page_config(page_title="Job Keyword Scanner", layout="centered")

st.title("Job Keyword Scanner") # Added an emoji to the title

st.write("Paste your resume and the job description below to analyze keyword match.")

resume = st.text_area("**Your Resume Text:**", height=300, placeholder="Paste your resume text here...")
job_desc = st.text_area("**Job Description Text:**", height=300, placeholder="Paste the job description here...")

if st.button("Analyze Job Fit", type="primary"): # Changed button text and added type for emphasis
    if resume and job_desc:
        match_pct, missing, score = compare_keywords(resume, job_desc)

        st.markdown("---") # Add a separator for better visual flow
        st.subheader("Analysis Results")

        # 1. Highlight Key Metric (Keyword Match)
        st.metric(label="Keyword Match Percentage", value=f"{match_pct:.2f}%")

        # 2. Visual Score Indicator
        st.write("---") # Another separator
        st.write("**Recommendation Score:**")
        if score == 'Excellent':
            st.success(f"**{score}!** Your resume is a strong match for this job description.")
        elif score == 'Good':
            st.info(f"**{score}!** A good match, but there's room for improvement.")
        elif score == 'Fair':
            st.warning(f"**{score}.** Consider optimizing your resume further.")
        else: # Needs Improvement
            st.error(f"**{score}.** Significant changes are needed to align with the job description.")

        st.write("---") # Another separator

        # 3. Cleaner Missing Keywords Display
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
                # Display missing keywords in a more readable format, e.g., as a bullet list or tagged items
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