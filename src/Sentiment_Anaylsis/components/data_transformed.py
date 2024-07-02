
from datasets import load_from_disk
from transformers import AutoTokenizer
from Sentiment_Anaylsis.entity import Datatransformationconfig






class Datatransformation:
    def __init__(self, config:Datatransformationconfig):
        self.config=config 
    
        self.dataset=load_from_disk(self.config.local_file)
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.source_name)
        self.tokenized=None

    def convert_examples_to_features(self, example):
        input_encodings = self.tokenizer(example['review'], max_length=128, truncation=True, padding='max_length')
        labels = [rating - 1 for rating in example['star']]

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': labels
        }
    def transformed(self):
        tokenized_datasets = self.dataset.map(self.convert_examples_to_features, batched=True)
        tokenized_datasets.save_to_disk(self.config.transformed_path)


