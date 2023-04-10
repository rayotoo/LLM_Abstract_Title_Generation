[![CodeQL](https://github.com/rayotoo/Abstract_Title_Generation/actions/workflows/codeql.yml/badge.svg)](https://github.com/rayotoo/Abstract_Title_Generation/actions/workflows/codeql.yml) [![Dependency Review](https://github.com/rayotoo/Abstract_Title_Generation/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/rayotoo/Abstract_Title_Generation/actions/workflows/dependency-review.yml) [![Bandit](https://github.com/rayotoo/Abstract_Title_Generation/actions/workflows/bandit.yml/badge.svg)](https://github.com/rayotoo/Abstract_Title_Generation/actions/workflows/bandit.yml)

# Summary Generator

This is a Python script that fine-tunes a Pegasus language model on a CSV file of text data, and uses the fine-tuned model to generate summaries of new text.

## Installation
This script requires Python 3.x, as well as several Python packages including pandas, transformers, sentencepiece, and torch. You can install these packages using pip, by running the following command:

```
pip install pandas transformers sentencepiece torch
```
Usage
To use this script, you'll need to provide a CSV file containing your text data. By default, the script assumes that the CSV file has columns named "title" and "abstract", and that these columns contain the text data to be summarized. You can modify the column names and data by editing the script accordingly.

Once you have your CSV file, you can run the script by running the following command:
```
python summary_generator_FineTuned.py
```
This will load the data from the CSV file, fine-tune the Pegasus model on the data, and generate summaries of new text using the fine-tuned model.

By default, the script generates summaries of the text contained in the "text" variable at the end of the script. You can modify this variable to contain your own text, and generate summaries of that text by running the script.

## Configuration
There are several configuration options available in the script, which you can modify to fine-tune the summarization process:

- model_name: This variable specifies the name of the pre-trained Pegasus model to use. By default, the script uses the "google/pegasus-xsum" model, which is a model fine-tuned on the CNN/Daily Mail dataset. You can replace this with the name of any other Pegasus model to use a different pre-trained model.

- train_batch_size: This variable specifies the batch size to use during training. By default, the script uses a batch size of 1, which can be slow on large datasets. You can increase this to a larger value (e.g. 4 or 8) to speed up training, but this may require more memory.

- num_train_epochs: This variable specifies the number of epochs to use during training. By default, the script uses 5 epochs, but you may need to increase this if your data is complex or if you want to achieve better summarization results.

- learning_rate: This variable specifies the learning rate to use during training. By default, the script uses a learning rate of 1e-5, which works well for most cases. You can experiment with higher or lower learning rates to see if this improves the summarization results.

- output_dir: This variable specifies the directory to save the fine-tuned model in. By default, the script saves the model in the current working directory, but you can specify a different directory if you prefer.

## Credits
This script uses the Pegasus language model from the Hugging Face Transformers library, as well as several other Python packages including pandas, sentencepiece, and torch. The script was written by [Your Name].





