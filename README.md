 # Trello

 [Trello Board](https://trello.com/b/Kd6QIMNx/my-money-app)

# Idea

The idea is a budget/money management app. The best way to describe my vision for the app is a lite version of [YNAB](https://www.youneedabudget.com/). My app initially will support csv files imported from the big 4 Aussie banks (Commbank, NAB, Westpac, ANZ)

My app will allow users to:

 - create/login to a personal account
 - create a budget linked to the users account
 - add/remove/edit transactions from a budget
 - filter transactions by date, amount, description
 - import transactions from a csv file to a budget
 - view net worth (graph?)
 - view income/expense

# Installation (Linux)

Install Python and git
```
sudo apt-get update
sudo apt-get install git
sudo apt-get install python3
```

Git clone and Open Folder
```
git clone https://github.com/HarryTranAU/my_money_app.git
cd my_money_app
```

Optional: Virtual Environment (Recommended)

```
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
```

Install Pip/requirements
```
sudo apt-get install python3-pip
pip install -r requirements.txt
```

# CI/CD Pipeline

**`Github Actions`**

 - [Setup Python (Github Marketplace)](https://github.com/marketplace/actions/setup-python)
 - Install dependencies
 - Run Tests (`unittest`)
 - Check Data Types (`mypy`)
 - Style Check (`flake8`) 

# Wireframes

## Login Page/Landing Page

![Login Page](docs/wireframes/Login_Page.png)

## Register User

![Register User Page](docs/wireframes/Register_User.png)

## Forgot User

![Forgot User Page](docs/wireframes/Forgot_User.png)

## User Settings

![User Settings Page](docs/wireframes/User_Settings.png)

## Budget Selection

![Budget Selection Page](docs/wireframes/Budget_Selection.png)

## Budget Overview

The Budget page is where the user will be creating their budget. The only editable fields should be the categories and budget columns. Activity column is where the transactions related to the category is summed up and shown. The Available column is the budget column minus the activity column. The user should be able to create and delete a category.

![Budget Overview Page](docs/wireframes/Budget_Overview.png)

## Accounts Page

![Accounts](docs/wireframes/Accounts.png)

## Reports - Cashflow

![Reports - Cashflow](docs/wireframes/Reports_Cashflow.png)

## Reports - Net Worth

![Reports - Net Worth](docs/wireframes/Reports_Net_Worth.png)


## Database

1. Each User can have multiple Budgets.
2. Each Budget can have multiple categories. E.g. Rent, Groceries, Utilities, Eating Out, etc.
3. Each Budget can have multiple Bank Accounts. E.g. Savings accounts, Credit Card account, etc.
4. Each Bank Account can have multiple Transactions.
5. Each Transaction can only have one Payee.
6. Each Payee can have multiple transactions. E.g. Multiple trips to Coles. Same Payee different transaction.
7. Each Payee can only belong to one Category. E.g. Coles cannot belong to both Groceries and Eating Out.
8. Each Category can have multiple Payees. E.g. Groceries category can have Coles, Woolworths, IGA, etc.


![Database Schema w/ crow feet notation](docs/database_schema_w_notation.png)

