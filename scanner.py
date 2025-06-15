import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    text = text.lower()
    words = word_tokenize(text)
    words = [re.sub(r'\W+', '', w) for w in words]
    words = [w for w in words if w]
    words = [w for w in words if w not in stopwords.words('english')]
    return set(words)

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
