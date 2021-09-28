from abc import ABC, abstractmethod
import argparse
import json
import os
from typing import Optional, List, Dict, Any

import pandas as pd


def setup_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-t', '--train', type=str, help='Train dataset path')
    parser.add_argument('-y', '--validation', type=str, help='Validation dataset path')
    parser.add_argument('-z', '--hyperparams', type=str, help='hyperparameters.json')
    parser.add_argument('-m', '--model', type=str, help='hyperparameters.json')
    parser.add_argument('cmd', nargs='+')
    return parser


class ExecutionContext(ABC):
    """
    Execution Context which can be sagemaker or commandline as a way to 
    collect inputs, configuration and hyperparameters
    """
    def __init__(self):
        pass

    @abstractmethod
    def train_path(self) -> str:
        pass

    @abstractmethod
    def validation_path(self) -> str:
        pass

    @abstractmethod
    def hyperparams_path(self) -> str:
        pass

    @abstractmethod
    def model_path(self) -> str:
        """
        :return: output path where to store model data
        """
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: train: {self.train_path()} validation: {self.validation_path()} model: {self.model_path()} hyperparms: {self.hyperparams_path()}"


class CommandlineContext(ExecutionContext):
    def __init__(self, args: List[str]=None):
        arg_parser: argparse.ArgumentParser = setup_arg_parser()
        self.cmd_args = arg_parser.parse_args(args)

    def train_path(self) -> str:
        return self.cmd_args.train

    def validation_path(self) -> str:
        return self.cmd_args.validation

    def hyperparams_path(self) -> str:
        return self.cmd_args.hyperparams

    def model_path(self) -> str:
        return self.cmd_args.model


class SageMakerContext(ExecutionContext):
    """

    /opt/ml/input/config/inputdataconfig.json
    """
    def __init__(self,
                 prefix: str="/opt/ml/",
                 model: str="model",
                 train: str="input/data/train",
                 validation: str="input/data/validation",
                 hyperparams: str="input/config/hyperparameters.json",
                 input_data_config: str="input/config/inputdataconfig.json",
                 resourceconfig: str="input/config/resourceconfig.json"
                 ):
        self.prefix = prefix
        self.model = os.path.join(prefix, model)
        self.train= os.path.join(prefix, train)
        self.validation = os.path.join(prefix, validation)
        self.hyperparams = os.path.join(prefix, hyperparams)
        self.input_data_config = os.path.join(prefix, input_data_config)
        self.resourceconfig = os.path.join(prefix, resourceconfig)

    def train_path(self) -> str:
        return self.train

    def validation_path(self) -> str:
        return self.validation

    def hyperparams_path(self) -> str:
        return self.hyperparams

    def model_path(self) -> str:
        return self.model

    @staticmethod
    def training_job_name() -> Optional[str]:
        return os.environ.get('TRAINING_JOB_NAME')

    @staticmethod
    def training_job_arn() -> Optional[str]:
        return os.environ.get('TRAINING_JOB_ARN')


def load_hyperparams(path: str) -> Dict[str, Any]:
    with open(path, "r") as f:
        return json.load(f)


def create_execution_context() -> ExecutionContext:
    if SageMakerContext.training_job_name():
        return SageMakerContext()
    else:
        return CommandlineContext()


def load_dataset(path: str, **kwargs) -> pd.DataFrame:
    return pd.read_csv(path, **kwargs)


class Hyperparams:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            self.__setattr__(k, v)

    def label_column(self) -> Optional[str]:
        # FIXME
        return None