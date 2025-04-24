import os
import urllib.request as request
import zipfile
import pandas as pd
from full_stack_mlops import logger
from full_stack_mlops.utils.common import get_size
from pathlib import Path
from full_stack_mlops.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

    def rename_columns(self):
        """
        Renames columns in the extracted CSV file
        """
        try:
            csv_path = os.path.join(self.config.unzip_dir, "winequality-white.csv")
            # Read the data without using first row as headers
            data = pd.read_csv(csv_path, header=None)

            # Define the column names we want to use
            column_names = [
                'fixed_acidity',
                'volatile_acidity',
                'citric_acid',
                'residual_sugar',
                'chlorides',
                'free_sulfur_dioxide',
                'total_sulfur_dioxide',
                'density',
                'pH',
                'sulphates',
                'alcohol',
                'quality'
            ]

            # Set the column names
            data.columns = column_names

            # Save the data back with proper column names
            data.to_csv(csv_path, index=False)
            logger.info(f"Columns renamed successfully. Shape of the data: {data.shape}")

        except Exception as e:
            logger.error(f"Error in renaming columns: {str(e)}")
            raise e
