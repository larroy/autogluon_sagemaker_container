from typing import Any
import os
from .common import ExecutionContext, load_dataset, Hyperparams, load_hyperparams
from autogluon.tabular import TabularPredictor


def train(ex: ExecutionContext) -> None:
    h: Hyperparams = Hyperparams(load_hyperparams(ex.hyperparams_path()))
    p: TabularPredictor = TabularPredictor(label="y", path=ex.model_path())
    train_df = load_dataset(ex.train_path())
    p.fit(train_data=train_df, hyperparameters={"GBM": {}})

