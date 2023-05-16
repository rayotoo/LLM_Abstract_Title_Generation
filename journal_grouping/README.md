# Large CSV File Processing

## Link to csv file
```
https://drive.google.com/file/d/1QCV45ysaz-2ghJyNkuh5NaoL9L2oxEKn/view?usp=sharing
```

This script processes a large CSV file containing 100,000 publications from the CORD-19 dataset and performs the following steps:

1. Reads an extremely large CSV file named "pruned_100000.csv" which contains publications from the CORD-19 dataset.
2. Subsets the data for the columns 'cord_uid', 'title', 'abstract', and 'journal'.
3. Counts the number of entries per journal.
4. Filters the top 10 journals with at least 100 entries.
5. Selects the first 100 entries from each of the selected journals, resulting in a total of 1000 rows.
6. Appends a column representing the journal with a number from 1 to 10.
7. Orders the results based on the journal number.
8. Writes the combined and ordered grouped journal data to a CSV file named "grouped_journals.csv".

## Prerequisites

- Python 3
- pandas library

## Usage

1. Download the script and place it in your desired location.
2. Place the "pruned_100000.csv" file, containing 100,000 publications from the CORD-19 dataset, in the same directory as the script.
3. Install the required dependencies by running the following command:
```
pip install pandas
```

4. Run the script using the following command:
```
python journal_grouping.py
```

Make sure to replace `script_name.py` with the actual name of the script file.

The script will process the CSV file and generate the "grouped_journals.csv" file with the combined and ordered grouped journal data.

Note: Adjust the `chunksize` value in the script based on your available memory to optimize processing large CSV files.

## License

This project is licensed under the [MIT License](LICENSE).

