import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    text = text.lower()
    words = word_tokenize(text)
    words = [re.sub(r'\W+', '', w) for w in words]
    words = [w for w in words if w and w not in stopwords.words('english')]
    return set(words)

def compare_keywords(resume, job_desc):
    resume_keywords = clean_text(resume)
    jd_keywords = clean_text(job_desc)
    
    matched = resume_keywords & jd_keywords
    missing = jd_keywords - resume_keywords
    
    match_pct = len(matched) / len(jd_keywords) * 100
    
    if match_pct >= 80:
        score = 'Excellent'
    elif match_pct >= 60:
        score = 'Good'
    else:
        score = 'Needs Improvement'
    
    return match_pct, missing, score

if __name__ == "__main__":
    resume = input("Paste your resume:\n")
    job_desc = input("Paste the job description:\n")
    
    match_pct, missing, score = compare_keywords(resume, job_desc)
    
    print(f"\nKeyword Match: {match_pct:.2f}%")
    print(f"Missing Keywords: {missing}")
    print(f"Recommendation: {score}")
