from flask import Blueprint, jsonify
from models.Budget import Budget
from schemas.BudgetSchema import budgets_schema
# from main import db
budgets = Blueprint("budgets", __name__, url_prefix="/budget")


# @budgets.route("/", methods=["POST"])
# def budget_create():
#     return "POST function"


@budgets.route("/", methods=["GET"])
def budget_index():
    budgets = Budget.query.all()
    serialised_data = budgets_schema.dump(budgets)
    return jsonify(serialised_data)


# @budgets.route("/", methods=["PUT"])
# def budget_update():
#     return "PUT function"


# @budgets.route("/", methods=["DELETE"])
# def budget_delete():
#     return "DELETE function"
