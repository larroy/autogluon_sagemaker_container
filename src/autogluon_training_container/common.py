from abc import ABC, abstractmethod

class ExecutionContext(ABC):
    """
    Execution Context which can be sagemaker or commandline as a way to 
    collect inputs, configuration and hyperparameters
    """
    def __init__(self, ):
        self.
    
    @abstractmethod
    def training_data_path() -> str:
        pass






class SageMakerContext(ExecutionContext):

