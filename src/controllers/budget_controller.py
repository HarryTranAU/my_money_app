from flask import Blueprint, jsonify, request, abort
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
    return jsonify(budgets_schema.dump(budgets))


@budgets.route("/<int:id>", methods=["GET"])
def budget_show(id):
    budget = Budget.query.get(id)
    return jsonify(budget_schema.dump(budget))


@budgets.route("/<int:id>", methods=["PUT", "PATCH"])
def budget_update(id):
    budgets = Budget.query.filter_by(id=id)
    budget_fields = budget_schema.load(request.json)
    budgets.update(budget_fields)
    db.session.commit()
    return jsonify(budget_schema.dump(budgets[0]))


@budgets.route("/<int:id>", methods=["DELETE"])
def budget_delete(id):
    budget = Budget.query.get(id)

    if not budget:
        return abort(404)

    db.session.delete(budget)
    db.session.commit()
    return jsonify(budget_schema.dump(budget))