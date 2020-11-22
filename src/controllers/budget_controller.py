from flask import Blueprint
budgets = Blueprint("budgets", __name__, url_prefix="/budget")


@budgets.route("/", methods=["POST"])
def budget_create():
    return "POST function"


@budgets.route("/", methods=["GET"])
def budget_index():
    return "GET function"


@budgets.route("/", methods=["PUT"])
def budget_update():
    return "PUT function"


@budgets.route("/", methods=["DELETE"])
def budget_delete():
    return "DELETE function"
