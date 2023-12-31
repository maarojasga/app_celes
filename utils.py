import logging
import os
from datetime import datetime

import pandas as pd

logging.basicConfig(level=logging.INFO)

DATA_FILE = os.getenv('DATA_FILE')


def read_data():
    """
    Reads sales data from the specified parquet file.
    The file path is obtained from an environment variable.
    """
    try:
        df = pd.read_parquet(DATA_FILE)
        return df
    except Exception as e:
        logging.error(f"Error reading the data file: {e}")
        return pd.DataFrame()


def sum_sales_by_column(key_column, key_value, start_date, end_date):
    """
    Calculates the sum of sales based on a specified key column (Employee, Product, Store)
    within a specified date range.
    """
    df = read_data()
    if df.empty:
        logging.warning("Dataframe is empty. No data to process.")
        return 0

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        mask = (df[key_column] == key_value) & (df['KeyDate'] >= start_date) & (df['KeyDate'] <= end_date)
        total = df.loc[mask, 'Amount'].sum()
        logging.info(f"Total sales calculated for {key_column} {key_value} from {start_date} to {end_date}")
        return total
    except Exception as e:
        logging.error(f"Error calculating sales: {e}")
        return 0


def sum_and_average_sales_by_column(key_column, key_value):
    """
    Calculates the total sum and average of sales based on a specified key column (Employee, Product, Store)
    without considering a date range.
    """
    df = read_data()
    if df.empty:
        logging.warning("Dataframe is empty. No data to process.")
        return 0, 0

    try:
        mask = (df[key_column] == key_value)
        total = df.loc[mask, 'Amount'].sum()
        average = df.loc[mask, 'Amount'].mean() if not df.loc[mask, 'Amount'].empty else 0
        logging.info(
            f"Total and average sales calculated for {key_column}: {key_value}, Total: {total}, Average: {average}")
        return total, average
    except Exception as e:
        logging.error(f"Error calculating sales: {e}")
        return 0, 0
