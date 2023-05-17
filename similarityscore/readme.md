# Similarity Score Analysis

This repository contains a Python script for calculating similarity scores and generating box plots based on the scores using word2vec word embeddings. The script reads a CSV file containing data and computes the similarity scores between title-abstract pairs and title-extractive summary pairs. It then generates box plots to visualize the distribution of similarity scores for the top 10 journals.

## Prerequisites

- Python 3.6 or above
- Required Python libraries: gensim, numpy, matplotlib

## Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/similarity-score-analysis.git

2. Navigate to the project directory:
```
cd similarity-score-analysis
```
3. Install the required Python libraries:
```
pip install gensim numpy matplotlib
```
4. Prepare the data:

Ensure that your data is in CSV format with the following columns:
'journal': Journal name
'title_abstract_score': Similarity score between title and abstract
'title_extractive_summary_score': Similarity score between title and extractive summary

5. Update the script:

Open the similarityScorePlot.py file in a text editor.
Modify the file path in line 10 to point to your CSV data file.

6. Run the script:
```
python similarityScorePlot.py
```
7. View the generated plots:

The generated plots will be displayed on the screen using the default system viewer.
