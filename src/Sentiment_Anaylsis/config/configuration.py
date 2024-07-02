from Sentiment_Anaylsis.constants import *
from Sentiment_Anaylsis.utils.common import read_yaml , create_directories
from Sentiment_Anaylsis.entity import Dataingestionconfig ,Datatransformationconfig

class ConfigurationManger:
    def __init__(self,config_file_path,params_file_path):
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

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