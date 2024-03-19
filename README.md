# Resume Parser and Scorer Application
This Flask application serves as a comprehensive Resume Parser and Scorer, designed to streamline the process of analyzing and evaluating resumes. Leveraging advanced techniques in web development, data extraction, and natural language processing (NLP), this application offers a robust solution for recruiters and hiring managers.

![Screenshot (252)](https://github.com/Aman18114312/Resume-Parser-and-Scorer/assets/129838853/937cf8a9-ec33-4cfb-8526-82c42f9164ce)

## Features
**Resume Parsing**: The application employs advanced Regex operations to meticulously extract relevant information such as skills, experience, and education from resume PDFs. This ensures accurate and comprehensive data extraction, facilitating efficient resume analysis.

**Resume Scoring**: Utilizing Natural Language Processing (NLP) operations, the application processes and analyzes the text corpus extracted from resumes. This enables the application to assign scores to resumes based on the relevance and depth of skills and experience present, providing valuable insights for recruiters.

**Compatibility Evaluation**: The application leverages cosine similarity as a robust metric to quantify the alignment between resume text and job descriptions. By calculating the similarity score, recruiters can assess the compatibility of candidates with specific job requirements accurately.

## Usage
**Upload Resumes**: Users can upload resumes in PDF format using the provided interface.
**Parsing and Scoring**: Upon upload, the application performs parsing and scoring operations to extract relevant information and assign scores to resumes.

**Compatibility Assessment**: Users can input job descriptions, and the application calculates the cosine similarity score to evaluate the compatibility of resumes with the specified job requirements.

**View Results**: The application displays parsed resume data, scores, and compatibility assessments for users to review.

## Technologies Used
**Flask**: Web application framework for Python.

**Regex**: Regular expressions for precise data extraction.

**Natural Language Processing (NLP)**: Techniques for text processing and analysis.

**Cosine Similarity**: Metric for evaluating similarity between text documents.
