from full_stack_mlops.config.configuration import ConfigurationManager
from full_stack_mlops.components.model_eval import ModelEvaluation
from full_stack_mlops import logger
import os

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        # Set MLflow tracking configuration
        os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/pvrraju6669/full-stack-mlops.mlflow"
        os.environ["MLFLOW_TRACKING_USERNAME"]="pvrraju6669"
        os.environ["MLFLOW_TRACKING_PASSWORD"]="0ec6d5287bb15fdf6c68db2cda31c27b934563bd"
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e