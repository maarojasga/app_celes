import unittest
from unittest.mock import patch

import pandas as pd

import utils

test_data = pd.DataFrame({
    'Employee': ['Alice', 'Bob', 'Alice', 'Bob'],
    'Product': ['X', 'Y', 'X', 'Y'],
    'Store': ['Store1', 'Store2', 'Store1', 'Store2'],
    'KeyDate': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']),
    'Amount': [100, 200, 150, 250]
})

test_data['KeyDate'] = test_data['KeyDate'].dt.date


class TestSalesFunctions(unittest.TestCase):

    @patch('utils.read_data', return_value=test_data)
    def test_sum_sales_by_column(self, mock_read_data):
        """
        Test calculates the sum of sales based on a specified key column (Employee, Product, Store)
        within a specified date range.
        """

        # In range
        total_sales = utils.sum_sales_by_column(
            'Employee', 'Alice', '2023-01-01', '2023-01-04')
        self.assertEqual(total_sales, 250)

        # Out range
        total_sales = utils.sum_sales_by_column(
            'Employee', 'Alice', '2023-01-05', '2023-01-06')
        self.assertEqual(total_sales, 0)

    @patch('utils.read_data', return_value=test_data)
    def test_sum_and_average_sales_by_column(self, mock_read_data):
        """
        Test calculates the sum and average sales
        within a specified date range.
        """
        # Exists
        total, average = utils.sum_and_average_sales_by_column('Employee', 'Bob')
        self.assertEqual(total, 450)
        self.assertEqual(average, 225)

        # Does not exist
        total, average = utils.sum_and_average_sales_by_column('Employee', 'Charlie')
        self.assertEqual(total, 0)
        self.assertEqual(average, 0)


if __name__ == '__main__':
    unittest.main()
