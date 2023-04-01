import pandas as pd
import numpy as np


def generate_month_list(start_date: pd.Timestamp = None,
                        end_date: pd.Timestamp = None) -> pd.DatetimeIndex:
    if start_date is None:
        start_date = pd.Timestamp.now().to_period('m')
    if end_date is None:
        end_date = pd.Timestamp.now().to_period('m')
    if start_date > end_date:
        raise ValueError("start_date must be earlier than end_date")

    formatted_dates = pd.period_range(start=start_date, end=end_date, freq='M')
    formatted_dates = formatted_dates.strftime('%Y-%m').tolist()

    return pd.DatetimeIndex(formatted_dates)

if __name__ == '__main__':
    [print(i) for i in generate_month_list('2023-01-15', '2023-03-15')]