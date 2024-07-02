
import os 
import datasets
from datasets import load_dataset
from Sentiment_Anaylsis.entity import Dataingestionconfig






class Dataingestion:
    def __init__(self, config:Dataingestionconfig):
        self.config=config 
    def save_data_huggingface(self):

        dataset=load_dataset(self.config.source_name)
        dataset.save_to_disk(self.config.local_file)