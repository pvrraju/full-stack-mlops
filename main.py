from full_stack_mlops import logger
from full_stack_mlops.pipeline.stage_01_data_ingest import DataIngestionTrainingPipeline




STAGE_NAME = "Data Ingestion Stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e
