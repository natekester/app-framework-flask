from sqlalchemy.dialects.postgresql import JSONB, ARRAY, ENUM
from . import db

example_enum_type = ENUM(
    "optionOne", "optionTwo", name="example_enum_type", create_type=False
)


class ExampleTable(db.Model):
    __tablename__ = "example_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    secondary_name = db.Column(db.String(100), nullable=True)

    # JSONB field for structured json data
    json = db.Column(JSONB, nullable=False)

    # Enum for attack type: "optionOne" or "optionTwo"
    enum_type = db.Column(example_enum_type, nullable=False)

    # Array of additional json types (e.g., ["fire", "poison"])
    array_example = db.Column(ARRAY(db.String), nullable=True)

    @classmethod
    def get_all(cls) -> list:
        return [row.to_dict() for row in cls.query.order_by("id").all()]

    def to_dict(self) -> dict[str, any]:
        return {
            "id": self.id,
            "name": self.name,
            "json": self.json,
            "enum_type": self.enum_type,
            "array_example": self.array_example,
        }
