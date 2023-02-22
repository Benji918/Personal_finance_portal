from datetime import date, timedelta
from typing import Dict, Union, List, Any


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
        result = (end_date.year - start_date.year) * 12
        result += (end_date.month - start_date.month)
        if end_date.day < start_date.day:  # if not full month passed
            result -= 1
        return result
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


# def calculate_repetitive_total(obj, last_balance_date, today, result_dict=None):
#     """Calculates the total value of a given object over a given time period.
#
#         Parameters:
#         obj (object): The object whose value is to be calculated.
#         last_balance_date (date): The start date of the time period.
#         today (date): The end date of the time period. If obj has a defined repetition_end date,
#                       the time period ends on that date instead of today.
#         result_dict (dict, optional): A dictionary to be populated with the value of the object
#                                       for each day in the time period. The keys of the dictionary
#                                       are the dates and the values are the amounts for those dates.
#                                       If not provided, the function returns the total value of the
#                                       object over the given time period.
#
#         Returns:
#         float or dict: If result_dict is not provided, returns the total value of the object over
#                        the given time period. If result_dict is provided, returns the result_dict
#                        with the values for each day in the time period.
#         """
#     total = 0
#     repetition_time = obj.repetition_time
#     end = obj.repetition_end if obj.repetition_end else today
#     if obj.repetition_interval == 2:  # DAYS
#         days_or_months = 'days'
#     elif obj.repetition_interval == 3:  # WEEKS
#         repetition_time = repetition_time * 7
#         days_or_months = 'days'
#     elif obj.repetition_interval == 4:  # MONTHS
#         if repetition_time % 30 == 0:  # assume months
#             days_or_months = 'months'
#             repetition_time = int(repetition_time / 30)
#         else:  # assume days
#             days_or_months = 'days'
#     elif obj.repetition_interval == 5:  # YEARS
#         repetition_time = repetition_time * 12
#         days_or_months = 'months'
#     else:
#         raise Exception('calculate_repetitive_total object repetition_interval can be only between 2 to 5 incl.')
#
#     balance_to_obj_time = calculate_interval_between_dates(obj.date, last_balance_date, days_or_months)
#     if balance_to_obj_time <= 0:
#         check_date = obj.date
#     else:
#         no_of_intervals_before = int(balance_to_obj_time / repetition_time)
#         check_date = add_interval_to_date(obj.date, days_or_months, repetition_time * no_of_intervals_before)
#
#     while last_balance_date >= check_date:
#         check_date = add_interval_to_date(check_date, days_or_months, repetition_time)
#     while check_date <= end:
#         if result_dict is None:
#             total += obj.value
#         else:
#             if result_dict is not None:
#                 result_dict[str(check_date)] = obj.value if str(check_date) not in result_dict \
#                     else result_dict[str(check_date)] + obj.value
#         check_date = add_interval_to_date(check_date, days_or_months, repetition_time)
#     return total if result_dict is None else result_dict


def calculate_repetitive_total(obj, last_balance_date, today):
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

    # Calculate the number of days between the last balance date and when the repetition ends
    days_since_last_balance = (end_date - last_balance_date).days

    # Calculate the number of repetitions that have occurred in that time period
    interval_days = calculate_interval_between_dates(obj.date, last_balance_date, days_or_months)
    repetitions = days_since_last_balance // interval_days

    # Calculate the total amount for those repetitions
    total = repetitions * obj.value

    # Calculate the next balance date after the last balance date
    next_balance_date = add_interval_to_date(last_balance_date, days_or_months, interval_days)

    # Calculate the balance date for each repetition and add the amount to the total
    balance_dates = []
    for i in range(repetitions):
        balance_date = next_balance_date + timedelta(days=interval_days * i)
        if balance_date > end_date:
            break
        balance_dates.append(balance_date)

    # Add the amount for each balance date to the total
    for balance_date in balance_dates:
        total += obj.value

    return total
