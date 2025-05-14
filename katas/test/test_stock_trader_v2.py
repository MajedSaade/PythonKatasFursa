import unittest
from katas.stock_trader_v2 import max_profit  # Replace with your actual filename


class TestMaxProfitMultipleTransactions(unittest.TestCase):

    def test_example_case(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 7)  # Buy at 1, sell at 5; buy at 3, sell at 6

    def test_monotonically_increasing(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(prices), 4)  # Buy at 1, sell at 5 (or buy/sell every day)

    def test_monotonically_decreasing(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)  # No profit possible

    def test_flat_prices(self):
        prices = [3, 3, 3, 3]
        self.assertEqual(max_profit(prices), 0)

    def test_empty_list(self):
        self.assertEqual(max_profit([]), 0)

    def test_single_price(self):
        self.assertEqual(max_profit([10]), 0)

    def test_multiple_rises_and_dips(self):
        prices = [1, 3, 2, 5, 4, 6]
        self.assertEqual(max_profit(prices), 7)  # (1→3)+(2→5)+(4→6)

    def test_peak_and_valley(self):
        prices = [1, 5, 2, 6, 3, 10]
        self.assertEqual(max_profit(prices), 15)  # (1→5)+(2→6)+(3→10)

    def test_alternating_up_and_down(self):
        prices = [1, 2, 1, 2, 1, 2]
        self.assertEqual(max_profit(prices), 3)

    def test_zero_profit_day_followed_by_rise(self):
        prices = [3, 3, 5]
        self.assertEqual(max_profit(prices), 2)


if __name__ == '__main__':
    unittest.main()
