from docx import Document
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#parse the docx
def parse_resume(docx_file):
    doc = Document(docx_file)
    
    # Initialize variables for extracted information
    extracted_text = ""
    
    # Iterate through paragraphs and extract text
    for paragraph in doc.paragraphs:
        extracted_text += paragraph.text + "\n"

    return extracted_text

#extract email
def extract_email(text):
    # Define a regular expression pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Search for the email address in the given text
    matches = re.findall(email_pattern, text)

    # Return the first match (if any)
    return matches[0] if matches else None

#extract name
def extract_name(text):
    # Regular expression pattern to match potential names
    name_pattern = re.compile(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b')

    # Search for potential names in the text
    matches = name_pattern.findall(text)

    # Return the first match (if any)
    return matches[0] if matches else None

#extract skills
def extract_skills(resume_text):
    # Define a regular expression pattern to match skills
    skills_pattern = re.compile(r'Skills\n(.+?)(\n\n|\nExperience|\nEducation|\nAwards)', re.DOTALL)
    
    # Search for skills in the resume text
    skills_match = skills_pattern.search(resume_text)
    
    # Extract and return skills if found
    if skills_match:
        skills_section = skills_match.group(1).strip()
        skills_list = [skill.strip() for skill in skills_section.split(',')]
        return skills_list
    else:
        return []

#extract experience
def extract_experience(text_data):
    experience_pattern = re.compile(r'\b(?:[A-Z][a-z]*:|Experience)\b(.+?)(?=\n(?:[A-Z][a-z]*:|Education|Awards|$))', re.DOTALL)
    experience_match = experience_pattern.search(text_data)
    experience = experience_match.group(1).strip() if experience_match else None
    return experience
    
#tokenise and remove stopwords
def tokenize_and_remove_stopwords(input_text):
    # Tokenize the text
    tokens = word_tokenize(input_text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]

    return filtered_tokens

#calculate similarity score 
def calculate_cosine_similarity(filtered_tokens, job_description_tokens):
    # Combine tokens into strings
    text_filtered_tokens = ' '.join(filtered_tokens)
    text_job_description = ' '.join(job_description_tokens)

    # Vectorize the text using TfidfVectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix_filtered_tokens = vectorizer.fit_transform([text_filtered_tokens])
    tfidf_matrix_job_description = vectorizer.transform([text_job_description])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix_filtered_tokens, tfidf_matrix_job_description)

    return cosine_sim[0][0]
