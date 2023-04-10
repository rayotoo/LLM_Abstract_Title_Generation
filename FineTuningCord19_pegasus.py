import pandas as pd
import time
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer, AdamW

# Load data from CSV file
data = pd.read_csv("cleaned_1000.csv")

# Get the column names of the dataframe
column_names = data.columns.tolist()

# Print the column names
print(column_names)

# Subset the dataframe to only include columns cord_uid, title, and abstract
data = data[['cord_uid', 'title', 'abstract']]

# Load pre-trained model and tokenizer
model_name = 'google/pegasus-xsum'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)

# Extract title and abstract columns as training data
train_data = [f"{title} </s> {abstract}" for title, abstract in zip(data['title'], data['abstract'])]

train_encodings = tokenizer(train_data, truncation=True, padding=True)

# Fine-tune the model
optimizer = AdamW(model.parameters(), lr=1e-5)
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model.to(device)

for epoch in range(5): # replace with number of epochs
    start_time = time.time()
    model.train()
    train_loss = 0

    for i in range(len(train_data)):
        input_ids = torch.tensor(train_encodings['input_ids'][i]).unsqueeze(0).to(device)
        attention_mask = torch.tensor(train_encodings['attention_mask'][i]).unsqueeze(0).to(device)
        labels = input_ids.clone().detach().to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs[0]

        train_loss += loss.item()

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

    end_time = time.time()
    epoch_time = end_time - start_time
    print(f'Epoch {epoch + 1} train loss: {train_loss / len(train_data)}, epoch time: {epoch_time:.2f} seconds')

# Save the fine-tuned model to the current directory
model.save_pretrained('./')

# Generate summaries using the fine-tuned model
model.eval()

text = 'The human gut microbiome impacts human brain health in numerous ways: (1) Structural bacterial components such as lipopolysaccharides provide low-grade tonic stimulation of the innate immune system. Excessive stimulation due to bacterial dysbiosis, small intestinal bacterial overgrowth, or increased intestinal permeability may produce systemic and/or central nervous system inflammation. (2) Bacterial proteins may cross-react with human antigens to stimulate dysfunctional responses of the adaptive immune system. (3) Bacterial enzymes may produce neurotoxic metabolites such as D-lactic acid and ammonia. Even beneficial metabolites such as short-chain fatty acids may exert neurotoxicity. (4) Gut microbes can produce hormones and neurotransmitters that are identical to those produced by humans. Bacterial receptors for these hormones influence microbial growth and virulence. (5) Gut bacteria directly stimulate afferent neurons of the enteric nervous system to send signals to the brain via the vagus nerve. Through these varied mechanisms, gut microbes shape the architecture of sleep and stress reactivity of the hypothalamic-pituitary-adrenal axis. They influence memory, mood, and cognition and are clinically and therapeutically relevant to a range of disorders, including alcoholism, chronic fatigue syndrome, fibromyalgia, and restless legs syndrome. Their role in multiple sclerosis and the neurologic manifestations of celiac disease is being studied. Nutritional tools'
input_ids = tokenizer.encode(text, return_tensors='pt').to(device)

summary_ids = model.generate(input_ids)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print(f'Original text: {text}')
print(f'Summary: {summary}')