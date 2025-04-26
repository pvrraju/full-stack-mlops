import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
# import mlflow.sklearn # Keep if other sklearn models might be logged
import mlflow.xgboost # Add xgboost mlflow import
import numpy as np
import joblib
from full_stack_mlops.utils.common import save_json
from pathlib import Path

from full_stack_mlops.entity.config_entity import ModelEvaluationConfig

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/pvrraju9/full-stack-mlops.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="pvrraju9"
os.environ["MLFLOW_TRACKING_PASSWORD"]="0ec6d5287bbd"
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    


    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]


        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)


            if tracking_url_type_store != "file":

            
                mlflow.xgboost.log_model(
                    xgb_model=model,
                    artifact_path="model",
                    registered_model_name="XGBoostModel"
                )
            else:
                mlflow.xgboost.log_model(xgb_model=model, artifact_path="model")

    
