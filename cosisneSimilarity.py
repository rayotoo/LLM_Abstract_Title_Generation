#pip install -U scikit-learn
#pip install -U scikit-learn scipy matplotlib

import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load CSV data
with open('new_file_with_summaries_and_titles.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Calculate cosine similarity scores
tfidf_vectorizer = TfidfVectorizer()
title_tfidf = tfidf_vectorizer.fit_transform([row['title'] for row in data])
abstract_summary_tfidf = tfidf_vectorizer.transform([row['abstract_summary'] for row in data])
extractive_summary_tfidf = tfidf_vectorizer.transform([row['extractive_summary'] for row in data])
abstract_summary_scores = cosine_similarity(title_tfidf, abstract_summary_tfidf)
extractive_summary_scores = cosine_similarity(title_tfidf, extractive_summary_tfidf)

# Add new columns to CSV data
for i, row in enumerate(data):
    row['abstract_summary_score'] = abstract_summary_scores[i][0]
    row['extractive_summary_score'] = extractive_summary_scores[i][0]

# Save CSV data with new columns
with open('cosineimilarity.csv', 'w', newline='') as file:
    fieldnames = ['cord_uid', 'title', 'abstract', 'abstract_summary', 'extractive_summary', 'suggested_title_bert', 'abstract_summary_score', 'extractive_summary_score']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
