from main import ma
from models.Budget import Budget
from schemas.UserSchema import UserSchema
from marshmallow.validate import Length


class BudgetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Budget

    name = ma.String(required=True, validate=Length(min=1))
    user = ma.Nested(UserSchema)


budget_schema = BudgetSchema()
budgets_schema = BudgetSchema(many=True)
