import os
from flask import Flask, render_template, request, jsonify
import function

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main():
    return render_template('index1.html')

@app.route('/parse', methods=['POST'])
def parse():
    resume_file = None
    if 'resume' not in request.files or request.files['resume'].filename == '':
        return jsonify({'error': 'No resume file uploaded'})

    if request.method == "POST":
        resume_file = request.files['resume']

    job_description = request.form.get('job_description', '')

    text_data = function.parse_resume(resume_file)

    skills = function.extract_skills(text_data)
    experience = function.extract_experience(text_data)

    # Preprocessing of skills and experience
    skills_and_experience = f"{skills} {experience}"
    skills_and_experience = function.tokenize_and_remove_stopwords(skills_and_experience)
    job_description = function.tokenize_and_remove_stopwords(job_description)

    # Calculate similarity between skills_and_experience vs job_description
    sim_score = function.calculate_cosine_similarity(skills_and_experience, job_description)

    name = function.extract_name(text_data)
    email = function.extract_email(text_data)

    return render_template('index1.html', score=sim_score, extracted_name=name, extracted_email=email, resume=resume_file)

if __name__ == "__main__":
    app.run(debug=True)
