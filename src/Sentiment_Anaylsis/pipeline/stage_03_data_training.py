
from datasets import load_from_disk
from transformers import AutoTokenizer
from Sentiment_Anaylsis.config.configuration import ConfigurationManger
from Sentiment_Anaylsis.components.data_training import Data_training



class DataTrainingPipeline:
    def __init__(self) :
        pass 
    def main(self):
       config=ConfigurationManger()
       datatraining_config=config.get_data_training_config()
       data_training=Data_training(config=datatraining_config)

    
       data_training.training_args()