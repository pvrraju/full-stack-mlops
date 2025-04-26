import pandas as pd
import os
from full_stack_mlops import logger
# from sklearn.linear_model import ElasticNet  # Comment out ElasticNet
import xgboost as xgb  # Import XGBoost
import joblib

from full_stack_mlops.entity.config_entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        xgb_model = xgb.XGBRegressor(
            n_estimators=self.config.n_estimators,
            learning_rate=self.config.learning_rate,
            max_depth=self.config.max_depth,
            subsample=self.config.subsample,
            colsample_bytree=self.config.colsample_bytree,
            gamma=self.config.gamma,
            reg_alpha=self.config.reg_alpha,
            reg_lambda=self.config.reg_lambda,
            random_state=42
        )

        xgb_model.fit(train_x, train_y)

        joblib.dump(xgb_model, os.path.join(self.config.root_dir, self.config.model_name))
        logger.info(f"XGBoost model saved to {os.path.join(self.config.root_dir, self.config.model_name)}")

