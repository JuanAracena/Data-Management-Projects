# TFIDF Document Similarity Project
### Project Description
This project is designed to illustrate the concepts of **TFIDF (Term Frequency-Inverse Document Frequency)** and how it can be used to determine the similarity between three documents based on certain words or phrases. The project does not use any library tools for TFIDF vectorization, instead, it is manually coded to understand the real-time calculations, steps, and formulas used to find word similarity within documents.

### Live Demo
A live demo of the project is not currently available.

### How to Build and Run
To run this project, follow these steps:
1. Prepare two text documents named "doc1" and "doc2" with the content you want to compare for similarities.
2. Download the 'tfidf.py' file.
3. Run the 'tfidf.py' file on your Python compiler along with the three text documents.

The progra will return three preprocessed documents (excluding stopwords and unnecessary symbols) and the final TFIDF documents with scores indicating the most similar words within the three documents.

### Tech Used
The project is developed using Python and does not rely on any external TFIDF vectorizer libraries.

### Development Process and Challenges
The development process involved manual coding to understand the underlying calculations, steps, and formulas used in TFIDF. This approach was chosen over using library tools to gain a deeper understanding of the process. The main challenge encountered was ensuring the accurate implementation of the TFIDF calculations and preprocessing the documents to exclude stopwords and unnecessary symbols. Despite these challenges, the project successfully returns the preprocessed documents and the final TFIDF scores.