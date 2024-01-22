from src.RedWineQualityPrediction.config.configuration import ConfigurationManager
from src.RedWineQualityPrediction.components.data_transformation import DataTransformation
from src.RedWineQualityPrediction import logger
from pathlib import Path


STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

                if status == "True":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(config = data_transformation_config)
                    data_transformation.train_test_splitting()
                else:
                    raise Exception ("This Data Schema is invalid!")
        except Exception as e: 
            print(e)


