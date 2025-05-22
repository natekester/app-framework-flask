from models.example_table import ExampleTable


class ModelFactory:
    @staticmethod
    def get_example_model() -> ExampleTable:
        return ExampleTable()
