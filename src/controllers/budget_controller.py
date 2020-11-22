from flask import Blueprint, jsonify, request
from models.Budget import Budget
from schemas.BudgetSchema import budgets_schema, budget_schema
from main import db
budgets = Blueprint("budgets", __name__, url_prefix="/budget")


@budgets.route("/", methods=["POST"])
def budget_create():
    budget_fields = budget_schema.load(request.json)
    new_budget = Budget()
    new_budget.name = budget_fields["name"]
    db.session.add(new_budget)
    db.session.commit()

    return jsonify(budget_schema.dump(new_budget))


@budgets.route("/", methods=["GET"])
def budget_index():
    budgets = Budget.query.all()
    serialised_data = budgets_schema.dump(budgets)
    return jsonify(serialised_data)

@budgets.route("/<int:id>", methods=["GET"])
def budget_show(id):
    budget = Budget.query.get(id)
    return jsonify(budget_schema.dump(budget))


# @budgets.route("/", methods=["PUT"])
# def budget_update():
#     return "PUT function"


# @budgets.route("/", methods=["DELETE"])
# def budget_delete():
#     return "DELETE function"
