import pandas as pd

# Step 1: Read the CSV file
csv_file = '/Users/raymondotoo/Desktop/nlp/pruned_100000.csv'
chunksize = 100000  # Adjust this value based on your available memory
dataframes = pd.read_csv(csv_file, iterator=True, chunksize=chunksize)

# Step 2: Subset the desired columns (cord_uid, title, abstract, journal)
selected_columns = ['cord_uid', 'title', 'abstract', 'journal']
subset_data = pd.concat([chunk[selected_columns] for chunk in dataframes])

# Step 3: Count the number of entries per journal
journal_counts = subset_data['journal'].value_counts()

# Step 4: Filter journals with at least 100 entries and select top 10
selected_journals = journal_counts[journal_counts > 100].index[:10]

# Step 5: Filter the first 100 entries from each of the selected journals
subset_data = subset_data[subset_data['journal'].isin(selected_journals)]
grouped_data = subset_data.groupby('journal').head(100)

# Step 6: Append a column representing the journal with a number from 1 to 10
journal_mapping = {journal: index + 1 for index, journal in enumerate(selected_journals)}
grouped_data['journal_number'] = grouped_data['journal'].map(journal_mapping)

# Step 7: Order the results based on journal_number
grouped_data = grouped_data.sort_values('journal_number')

# Step 8: Write the combined grouped data to a CSV file
output_file = 'grouped_journals.csv'
grouped_data.to_csv(output_file, index=False)

print(f"Combined and ordered grouped journal data has been written to {output_file}.")


