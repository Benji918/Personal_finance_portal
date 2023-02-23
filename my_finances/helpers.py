from datetime import datetime, timedelta, date
from typing import Dict, Union, List, Any

from dateutil import relativedelta


def calculate_interval_between_dates(start_date, end_date, days_or_months):
    """
     Calculate the interval between two dates in either days or months.
     Parameters:
         start_date (datetime.datetime): The start date.
         end_date (datetime.datetime): The end date.
         days_or_months (str): A string indicating whether to calculate the interval in days or months. Must be either
             'days' or 'months'.
     Returns:
         int or float: The interval between the two dates in either days or months, depending on the value of
             `days_or_months`.
     Raises:
         ValueError: If `days_or_months` is not 'days' or 'months'.
     """
    if days_or_months == 'days':
        return (end_date - start_date).days
    elif days_or_months == 'months':
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
        end_date = datetime.strptime(end_date, "%d/%m/%Y")
        # Get the relative-delta between two dates
        result = relativedelta.relativedelta(end_date, start_date)
        return result.days
    else:
        raise ValueError('add_interval_to_date accepts only str "days" or "months" for days_or_months')


def add_interval_to_date(original_date: date, days_or_months: str, value: int) -> Union[date, Exception, list]:
    """
       Add a specified number of days or months to a given date

       Parameters:
           original_date (date): The original date. Can be a single date or a list of dates.
           days_or_months (str): A string indicating whether to add days or months. Must be either 'days' or 'months'.
           value (int): The number of days or months to add.

       Returns:
           date or list of dates: The resulting date(s) after adding the specified interval.

       Raises:
           ValueError: If `days_or_months` is not 'days' or 'months'.
       """
    if days_or_months == 'days':
        return original_date + timedelta(days=value)
    elif days_or_months == 'months':
        y, m = divmod(original_date.month + value, 12)
        if m == 0:
            m = 12
            y = y - 1
        y += original_date.year
        d = original_date.day
        return date(y, m, d)
    else:
        raise ValueError('add_interval_to_date accepts only str "days" or "months" for days_or_months')


def calculate_repetitive_total(obj, today):
    """Calculates the total value of a given object over a given time period.

        Parameters:
        obj (object): The object whose value is to be calculated.
        last_balance_date (date): The start date of the time period.
        today (date): The end date of the time period. If obj has a defined repetition_end date,
                      the time period ends on that date instead of today.
        result_dict (dict, optional): A dictionary to be populated with the value of the object
                                      for each day in the time period. The keys of the dictionary
                                      are the dates and the values are the amounts for those dates.
                                      If not provided, the function returns the total value of the
                                      object over the given time period.

        Returns:
        float or dict: If result_dict is not provided, returns the total value of the object over
                       the given time period. If result_dict is provided, returns the result_dict
                       with the values for each day in the time period.
        """
    total = 0
    repetition_time = obj.repetition_time
    end_date = obj.repetition_end if obj.repetition_end else today
    if obj.repetition_interval == 2:  # DAYS
        days_or_months = 'days'
    elif obj.repetition_interval == 3:  # WEEKS
        repetition_time = repetition_time * 7
        days_or_months = 'days'
    elif obj.repetition_interval == 4:  # MONTHS
        days_or_months = 'months'
    elif obj.repetition_interval == 5:  # YEARS
        repetition_time = repetition_time * 12
        days_or_months = 'months'
    else:
        raise Exception('calculate_repetitive_total object repetition_interval can be only between 2 to 5 incl.')

    # Calculate the number of days between the last balance date and today
    diff_btw_start_and_end_date = calculate_interval_between_dates(start_date=obj.date, end_date=end_date,
                                                                   days_or_months=days_or_months)

    # Calculate the balance dates for each repetition
    balance_dates = []
    for i in range(diff_btw_start_and_end_date):
        balance_date = obj.date + timedelta(days=i)
        if balance_date > end_date:
            break
        balance_dates.append(balance_date)

    # Add the amount for each balance date to the total
    for balance_date in balance_dates:
        total += obj.value

    return total
