from full_stack_mlops import logger
from full_stack_mlops.pipeline.stage_01_data_ingest import DataIngestionTrainingPipeline
from full_stack_mlops.pipeline.stage_02_data_validate import DataValidationTrainingPipeline
from full_stack_mlops.pipeline.stage_03_data_tranform import DataTransformationTrainingPipeline
from full_stack_mlops.pipeline.state_04_model_train import ModelTrainerTrainingPipeline
from full_stack_mlops.pipeline.stage_05_model_evaluate import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
if __name__ == "__main__":
    try:
        logger.info(f"*#*#*#*#*#*#*#*# stage {STAGE_NAME} started $@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*# stage {STAGE_NAME} completed $@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation Stage"
if __name__ == "__main__":
    try:
        logger.info(f"*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*# stage {STAGE_NAME} started $@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*# stage {STAGE_NAME} completed $@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation Stage"
if __name__ == "__main__":
    try:
        logger.info(f"*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*# stage {STAGE_NAME} started $@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*# stage {STAGE_NAME} completed $@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer stage"
if __name__ == "__main__":
    try:
        logger.info(f"*#*#*#*#*#*# stage {STAGE_NAME} started $@$@$@$@$@$@") 
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f"*#*#*#*#*#*# stage {STAGE_NAME} completed $@$@$@$@$@$@\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Evaluation stage"
if __name__ == "__main__":
    try:
        logger.info(f"*#*#*#*#*#*# stage {STAGE_NAME} started $@$@$@$@$@$@") 
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f"*#*#*#*#*#*# stage {STAGE_NAME} completed $@$@$@$@$@$@\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e