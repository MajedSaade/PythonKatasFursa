import unittest
from katas.stock_trader import max_profit  # Replace with actual filename


class TestMaxProfit(unittest.TestCase):

    def test_regular_profit(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 5)  # Buy at 1, sell at 6

    def test_no_profit(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)  # No rising prices

    def test_max_profit_at_end(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(prices), 4)  # Buy at 1, sell at 5

    def test_max_profit_at_start(self):
        prices = [5, 4, 3, 10]
        self.assertEqual(max_profit(prices), 7)  # Buy at 3, sell at 10

    def test_flat_prices(self):
        prices = [3, 3, 3, 3]
        self.assertEqual(max_profit(prices), 0)

    def test_single_price(self):
        self.assertEqual(max_profit([10]), 0)

    def test_empty_list(self):
        self.assertEqual(max_profit([]), 0)

    def test_price_dips_and_rises(self):
        prices = [2, 4, 1, 7]
        self.assertEqual(max_profit(prices), 6)  # Buy at 1, sell at 7

    def test_profit_with_zero_price(self):
        prices = [0, 1, 2, 3]
        self.assertEqual(max_profit(prices), 3)

    def test_large_first_drop(self):
        prices = [100, 1, 2, 3, 4]
        self.assertEqual(max_profit(prices), 3)  # Buy at 1, sell at 4


if __name__ == '__main__':
    unittest.main()
