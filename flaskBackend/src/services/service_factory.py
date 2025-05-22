from services.example_service import ExampleService

from models.model_factory import ModelFactory


class ServiceFactory:
    @staticmethod
    def get_example_service() -> ExampleService:
        exampleModel = ModelFactory.get_example_model()
        return ExampleService(exampleModel)
