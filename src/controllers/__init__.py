from controllers.budget_controller import budgets
from commands import db_commands
from controllers.auth_controller import auth

registerable_controllers = [
    budgets,
    db_commands,
    auth
]