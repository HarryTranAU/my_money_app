import unittest
from main import create_app, db
from models.Budget import Budget


class TestBudgets(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-custom", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_budget_index(self):
        response = self.client.get("/budget/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_budget_create(self):
        response = self.client.post("/budget/", json={
            "name": "Test Budget"
        })

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertTrue(bool("id" in data.keys()))

        budget = Budget.query.get(data["id"])
        self.assertIsNotNone(budget)

    def test_budget_delete(self):
        budget = Budget.query.first()

        response = self.client.delete(f"/budget/{budget.id}")

        self.assertEqual(response.status_code, 200)

        budget = Budget.query.get(budget.id)
        self.assertIsNone(budget)
