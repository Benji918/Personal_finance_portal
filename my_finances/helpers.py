from datetime import date, timedelta


def calculate_interval_between_dates(start_date, end_date, days_or_months):
    if days_or_months == 'days':
        return (end_date - start_date).days
    elif days_or_months == 'months':
        result = (end_date.year - start_date.year) * 12
        result += (end_date.month - start_date.month)
        if end_date.day < start_date.day:  # if not full month passed
            result -= 1
        return result
    else:
        raise Exception('add_interval_to_date accepts only str "days" or "months" for days_or_months')


def add_interval_to_date(original_date, days_or_months, value):
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
        raise Exception('add_interval_to_date accepts only str "days" or "months" for days_or_months')


def calculate_repetitive_total(obj, last_balance_date, today, result_dict=None):
    total = 0
    repetition_time = obj.repetition_time
    end = obj.repetition_end if obj.repetition_end else today
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

    balance_to_obj_time = calculate_interval_between_dates(obj.date, last_balance_date, days_or_months)
    if balance_to_obj_time <= 0:
        check_date = obj.date
    else:
        no_of_intervals_before = int(balance_to_obj_time / repetition_time)
        check_date = add_interval_to_date(obj.date, days_or_months, repetition_time * no_of_intervals_before)

    while last_balance_date >= check_date:
        check_date = add_interval_to_date(check_date, days_or_months, repetition_time)
    while check_date <= end:
        if result_dict is None:
            total += obj.value
        else:
            result_dict[str(check_date)] = obj.value if str(check_date) not in result_dict \
                else result_dict[str(check_date)] + obj.value
        check_date = add_interval_to_date(check_date, days_or_months, repetition_time)
    return total if result_dict is None else result_dict
