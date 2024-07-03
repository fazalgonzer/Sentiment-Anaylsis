from Sentiment_Anaylsis.constants import *
from Sentiment_Anaylsis.utils.common import read_yaml , create_directories
from Sentiment_Anaylsis.entity import Dataingestionconfig ,Datatransformationconfig ,Datatrainingconfig ,PredictionConfig
CONFIG_FILE_PATH=Path("config.yaml")
PARAMS_FILE_PATH=Path("params.yaml")
class ConfigurationManger:
    def __init__(self):
        self.config=read_yaml(CONFIG_FILE_PATH)
        self.params=read_yaml(PARAMS_FILE_PATH)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> Dataingestionconfig:
        config=self.config.data_ingestion

        create_directories([config.root_dir])


        data_ingestion_config=Dataingestionconfig(


            root_dir=config.root_dir,


            
            source_name= config.source_name,
            local_file=config.local_file
                
        )
        return data_ingestion_config
    


    def get_data_transformation_config(self) -> Datatransformationconfig:
        config=self.config.data_transformation

        create_directories([config.root_dir])
        data_transformation_config=Datatransformationconfig(


            root_dir=config.root_dir,


            
            source_name= config.source_name,
           
            local_file=config.local_file,
            transformed_path=config.transformed_path

                
        )
      
        return data_transformation_config
    

    def get_data_training_config(self) -> Datatrainingconfig:
        config=self.config.data_training

        create_directories([config.root_dir])
        data_training_config=Datatrainingconfig(


            root_dir=config.root_dir,


            
            source_name= config.source_name,
           
           
            transformed_path=config.transformed_path,
            saving_model=config.saving_model

                
        )
      
        return data_training_config
    

    def get_prediction_config(self) -> PredictionConfig:
        config=self.config.prediction

        create_directories([config.root_dir])
        prediction_config=PredictionConfig(


            root_dir=config.root_dir,


            
            source_name= config.source_name,
           
           
                
        )
      
        return prediction_config
