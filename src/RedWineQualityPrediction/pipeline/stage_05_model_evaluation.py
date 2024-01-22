from src.RedWineQualityPrediction.config.configuration import ConfigurationManager
from src.RedWineQualityPrediction.components.model_evaluation import ModelEvaluate
from src.RedWineQualityPrediction import logger
from pathlib import Path


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluate_config = config.get_model_evaluation_config()
        model_evaluate = ModelEvaluate(config = model_evaluate_config)
        model_evaluate.save_results()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=================x")
    except Exception as e:
        logger.exception(e)
        raise e