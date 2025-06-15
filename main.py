import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data (only once, then you can comment it)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Text cleaning and keyword extraction
def clean_text(text):
    text = text.lower()  # lowercase everything
    words = word_tokenize(text)  # tokenize
    words = [re.sub(r'\W+', '', w) for w in words]  # remove non-word characters
    words = [w for w in words if w]  # remove empty strings
    words = [w for w in words if w not in stopwords.words('english')]  # remove stopwords
    return set(words)

# Keyword comparison logic
def compare_keywords(resume, job_desc):
    resume_keywords = clean_text(resume)
    jd_keywords = clean_text(job_desc)

    matched = resume_keywords & jd_keywords
    missing = jd_keywords - resume_keywords

    match_pct = (len(matched) / len(jd_keywords)) * 100 if jd_keywords else 0

    if match_pct >= 80:
        score = 'Excellent'
    elif match_pct >= 60:
        score = 'Good'
    elif match_pct >= 40:
        score = 'Fair'
    else:
        score = 'Needs Improvement'

    return match_pct, sorted(missing), score

# Main CLI function
def main():
    print("🚀 Job Keyword Scanner 🚀\n")
    
    resume = input("Paste your resume text:\n")
    print("\n---\n")
    job_desc = input("Paste the job description text:\n")

    match_pct, missing, score = compare_keywords(resume, job_desc)

    print("\n=== Results ===")
    print(f"Keyword Match: {match_pct:.2f}%")
    print(f"Missing Keywords: {', '.join(missing) if missing else 'None'}")
    print(f"Recommendation: {score}")

if __name__ == "__main__":
    main()
