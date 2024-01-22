from src.RedWineQualityPrediction.config.configuration import ConfigurationManager
from src.RedWineQualityPrediction.components.model_trainer import ModelTrainer
from src.RedWineQualityPrediction import logger
from pathlib import Path


STAGE_NAME = "Model Trainer Stage"

class ModelTrainerConfigTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)
        model_trainer.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainerConfigTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=================x")
    except Exception as e:
        logger.exception(e)
        raise e
