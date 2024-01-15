import unittest
from deposit import deposits


class TestDepositSelection(unittest.TestCase):


    def test_deposit_selection(self):
        initial_sum = 1000
        period = 12


        matched_deposits = []
        for deposit in deposits:
            try:
                deposit._check_user_params(initial_sum, period)
                matched_deposits.append(deposit)
            except AssertionError as err:
                pass


        self.assertEqual(len(matched_deposits), 3)


        expected_results = [
            {
                "name": "Сохраняй",
                "profit": 50.0,
                "sum": 1050.0,
                "currency": "руб."
            },
            {
                "name": "Бонусный 2",
                "profit": 52.5,
                "sum": 1052.5,
                "currency": "руб."
            },
            {
                "name": "С капитализацией",
                "profit": 51.16,
                "sum": 1051.16,
                "currency": "руб."
            }
        ]


        for i, deposit in enumerate(matched_deposits):
            self.assertEqual(deposit.name, expected_results[i]["name"])
            self.assertEqual(deposit.get_profit(initial_sum, period), expected_results[i]["profit"])
            self.assertEqual(deposit.get_sum(initial_sum, period), expected_results[i]["sum"])
            self.assertEqual(deposit.currency, expected_results[i]["currency"])


if __name__ == '__main__':
    unittest.main()
