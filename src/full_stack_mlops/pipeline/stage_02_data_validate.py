from full_stack_mlops.config.configuration import ConfigurationManager
from full_stack_mlops.components.data_validate import DataValidation
from full_stack_mlops import logger


STAGE_NAME = "Data Validation Stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e