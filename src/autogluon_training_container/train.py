from typing import Any
import os

def train(model_out: str, train_dataset_path: str, test_dataset_path: str) -> None:
    pass


def runnin_in_sm() -> bool:
    """
    :return: True if running in SM as a processing job
    """
    return "TRAINING_JOB_NAME" in os.environ


def hyperparams_path() -> str:
    """Get path for hyperparameter file in SM"""




def get_hyperparams(path: str) -> Dict[str, Any]

def train_sagemaker() -> None:
    hyperparams = get_hyperparams(
