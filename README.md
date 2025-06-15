# Job Keyword Scanner

Live Website: https://job-keyword-scanner-eduardo-bennaton.streamlit.app/

A lightweight and interactive web application built with Streamlit that helps job seekers analyze the alignment between their resume and a job description based on keyword matching. This tool assists users in optimizing their resumes by identifying missing keywords and estimating the relevance of their current resume for a given job posting.

## Features

- **Keyword Comparison**: Extracts and compares keywords from both resume and job description.
- **Match Percentage**: Displays how well your resume matches the job based on keyword overlap.
- **Recommendation Score**: Provides qualitative feedback (Excellent, Good, Fair, Needs Improvement) depending on your keyword match.
- **Missing Keywords**: Lists keywords found in the job description but missing from the resume.
- **Modern UI**: Simple, intuitive, and responsive interface using Streamlit.
- **Natural Language Processing (NLP)**: Utilizes NLTK for tokenization, stopword removal, and text cleaning.

## Technologies Used

- **Python**: Core language for processing and analysis.
- **Streamlit**: Framework for building the interactive web app.
- **NLTK (Natural Language Toolkit)**: Used for text preprocessing, tokenization, and stopword removal.
- **Regex**: Cleans and standardizes text data for accurate comparison.

### How to Run

To get this Job Keyword Scanner up and running on your local machine:

1.  **Ensure you have Python installed** (Python 3.8+ recommended).
2.  **Create a virtual environment** (recommended for managing dependencies):
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    * On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    * On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
3.  **Install the required libraries**:
    ```bash
    pip install streamlit nltk
    ```
4.  **Run the Streamlit application**:
    Assuming your Streamlit application file is named `app.py` and the `scanner.py` file is in the same directory:
    ```bash
    streamlit run app.py
    ```
    (If your main Streamlit file has a different name, replace `app.py` with its actual name.)

This will open the application in your default web browser, usually at `http://localhost:8501`.

## Project Structure

project_root/
│
├── app.py # Main Streamlit application
├── scanner.py # Core keyword extraction and comparison logic
├── README.md # This file
└── requirements.txt # (Optional) Dependency list for easy installation
