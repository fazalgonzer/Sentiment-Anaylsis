from Sentiment_Anaylsis.config.configuration import ConfigurationManger
from Sentiment_Anaylsis.components.prediction import PredictionF






class Prediction:
    def __init__(self,text) :
        self.text=text
        
    def predict(self):
        config=ConfigurationManger()
        prediction_config=config.get_prediction_config()
        pred=PredictionF(config=prediction_config)
        label,probs=pred.prediction(self.text)
        return label