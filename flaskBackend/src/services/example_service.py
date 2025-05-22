class ExampleService:
    def __init__(self, exampleRepo):
        self.exampleRepo = exampleRepo

    def get_all_examples(self):
        return self.exampleRepo.get_all()

    def create_example_record(self, name, damage, type_):
        return self.exampleRepo.save({"name": name, "damage": damage, "type": type_})
