from full_stack_mlops.config.configuration import ConfigurationManager
from full_stack_mlops.components.data_tranform import DataTransformation
from full_stack_mlops import logger
from pathlib import Path


SRAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("You data schema is not valid.")
        except Exception as e:
            print(e)