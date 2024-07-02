

from Sentiment_Anaylsis.config.configuration import ConfigurationManger
from pathlib import Path
from Sentiment_Anaylsis.components.data_ingestion import Dataingestion








class DataingestionConfigTrainingPipeline:
    def __init__(self) :
        pass 
    def main(self):
        config=ConfigurationManger(config_file_path=Path("config.yaml"),params_file_path=Path("params.yaml"))
        dataingestion_config=config.get_data_ingestion_config()
        data_ingestion=Dataingestion(config=dataingestion_config)
        data_ingestion.save_data_huggingface()