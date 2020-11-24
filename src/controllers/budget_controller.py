from models.Budget import Budget
from models.User import User
from main import db
from schemas.BudgetSchema import budgets_schema, budget_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request, abort
from sqlalchemy.orm import joinedload
budgets = Blueprint("budgets", __name__, url_prefix="/budget")


@budgets.route("/", methods=["POST"])
@jwt_required
def budget_create():
    budget_fields = budget_schema.load(request.json)
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")

    new_budget = Budget()
    new_budget.name = budget_fields["name"]

    user.budgets.append(new_budget)
    db.session.commit()

    return jsonify(budget_schema.dump(new_budget))


@budgets.route("/", methods=["GET"])
def budget_index():
    budgets = Budget.query.options(joinedload("user")).all()
    return jsonify(budgets_schema.dump(budgets))


@budgets.route("/<int:id>", methods=["GET"])
def budget_show(id):
    budget = Budget.query.get(id)
    return jsonify(budget_schema.dump(budget))


@budgets.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
def budget_update(id):
    budget_fields = budget_schema.load(request.json)
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")

    budgets = Budget.query.filter_by(id=id, user_id=user.id)
    
    if budgets.count() != 1:
        return abort(401, description="Unauthorized to update this book")

    budgets.update(budget_fields)
    db.session.commit()

    return jsonify(budget_schema.dump(budgets[0]))


@budgets.route("/<int:id>", methods=["DELETE"])
@jwt_required
def budget_delete(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")

    budget = Budget.query.filter_by(id=id, user_id=user.id).first()

    if not budget:
        return abort(400)

    db.session.delete(budget)
    db.session.commit()

    return jsonify(budget_schema.dump(budget))
