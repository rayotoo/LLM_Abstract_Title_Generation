import csv
import numpy as np
import matplotlib.pyplot as plt

# Load CSV data with the appropriate encoding
with open('cosine_similarity_word2vec.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Extract the journal names and similarity scores
journals = [row['journal'] for row in data]
title_abstract_scores = [float(row['title_abstract_score']) if row['title_abstract_score'] else 0 for row in data]
title_extractive_summary_scores = [float(row['title_extractive_summary_score']) if row['title_extractive_summary_score'] else 0 for row in data]

# Create a dictionary to store scores for each journal
journal_scores = {}
for journal, score1, score2 in zip(journals, title_abstract_scores, title_extractive_summary_scores):
    if journal not in journal_scores:
        journal_scores[journal] = {'title_abstract_scores': [], 'title_extractive_summary_scores': []}
    journal_scores[journal]['title_abstract_scores'].append(score1)
    journal_scores[journal]['title_extractive_summary_scores'].append(score2)

# Get the top 10 journals based on the number of articles
top_journals = sorted(journal_scores.keys(), key=lambda x: len(journal_scores[x]['title_abstract_scores']), reverse=True)[:10]

# Extract the scores for the top 10 journals
scores_title_abstract = [journal_scores[journal]['title_abstract_scores'] for journal in top_journals]
scores_title_extractive_summary = [journal_scores[journal]['title_extractive_summary_scores'] for journal in top_journals]

# Plot the title-abstract similarity scores
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(scores_title_abstract, positions=np.arange(len(top_journals)), widths=0.4, patch_artist=True)
ax.set_xticks(np.arange(len(top_journals)))
ax.set_xticklabels(top_journals, rotation=45, ha='right')
ax.set_xlabel('Journal')
ax.set_ylabel('Similarity Score')
ax.set_title('Box Plot of Title-Abstract Similarity Scores for Top 10 Journals')
plt.tight_layout()

# Add color to the title-abstract plot
colors_title_abstract = ['lightblue', 'lightgreen', 'lightpink', 'lightyellow', 'lightcyan',
                         'lightsalmon', 'lightgray', 'lightcoral', 'lightseagreen', 'lightsteelblue']
for patch, color in zip(ax.artists, colors_title_abstract):
    patch.set_facecolor(color)

plt.show()

# Plot the title-extractive summary similarity scores
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(scores_title_extractive_summary, positions=np.arange(len(top_journals)), widths=0.4, patch_artist=True)
ax.set_xticks(np.arange(len(top_journals)))
ax.set_xticklabels(top_journals, rotation=45, ha='right')
ax.set_xlabel('Journal')
ax.set_ylabel('Similarity Score')
ax.set_title('Box Plot of Title-Extractive Summary Similarity Scores for Top 10 Journals')
plt.tight_layout()

# Add color to the title-extractive summary plot
colors_title_extractive_summary = ['lightblue', 'lightgreen', 'lightpink', 'lightyellow', 'lightcyan',
                                   'lightsalmon', 'lightgray', 'lightcoral', 'lightseagreen', 'lightsteelblue']
for patch, color in zip(ax.artists, colors_title_extractive_summary):
    patch.set_facecolor(color)

plt.show()
