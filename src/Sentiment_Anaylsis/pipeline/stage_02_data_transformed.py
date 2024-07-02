
from datasets import load_from_disk
from transformers import AutoTokenizer
from Sentiment_Anaylsis.entity import Datatransformationconfig


from Sentiment_Anaylsis.config.configuration import ConfigurationManger
from Sentiment_Anaylsis.components.data_transformed import Datatransformation






class DatatrnsformationTrainingPipeline:
    def __init__(self) :
        pass 
    def main(self):
        config=ConfigurationManger()
        datatransformation_config=config.get_data_transformation_config()
        data_transformation=Datatransformation(config=datatransformation_config)

    
        data_transformation.transformed()