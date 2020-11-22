from main import ma
from models.Budget import Budget


class BudgetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Budget


budget_schema = BudgetSchema()
budgets_schema = BudgetSchema(many=True)