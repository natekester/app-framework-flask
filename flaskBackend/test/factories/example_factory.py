from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker
from models.example_table import ExampleTable, db, example_enum_type

print("about to import factory")
import factory

fake = Faker()


class ExampleFactory(SQLAlchemyModelFactory):
    class Meta:
        model = ExampleTable
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    name = factory.LazyAttribute(lambda _: fake.name())
    array_example = factory.LazyFunction(lambda: [fake.name()])
    secondary_name = factory.LazyAttribute(lambda _: fake.name())
    json = factory.LazyFunction(
        lambda: {
            "id": fake.uuid4(),
            "tags": fake.words(nb=3),
            "active": fake.boolean(),
        }
    )
    enum_type = factory.LazyAttribute(lambda _: "optionOne")
