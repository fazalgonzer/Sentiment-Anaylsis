from transformers import AutoModelForSequenceClassification,AutoTokenizer
import torch
from Sentiment_Anaylsis.config.configuration import PredictionConfig


class Prediction:
     def __init__(self, config:PredictionConfig):
        self.config=config 
        self.model = AutoModelForSequenceClassification.from_pretrained(self.config.source_name,num_labels=5)
        self.tokenizer= AutoTokenizer.from_pretrained(self.config.source_name)
        

     def prediction(self,text):
         
         inputs = self.tokenizer(text, return_tensors="pt")
         
         with torch.no_grad():
            outputs = self.model(**inputs)
    
         # Get the predicted label (logits)
         logits = outputs.logits
         
         # Convert logits to probabilities
         probabilities = torch.softmax(logits, dim=1)
         
         # Get the label with the highest probability
         predicted_label = torch.argmax(probabilities, dim=1).item()
         
         return predicted_label, probabilities



         
         return predicted_label , probabilities