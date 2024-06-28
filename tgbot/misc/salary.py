async def salary_with_percents(
    position: str,
    hourly_payment: int,
    hours_worked: int,
    coefficient: float,
    aht: int,
    flr: int,
    gok: int,
    client_rating: int = 0,
    tests: str = 0,
    sl: int = 0,
):
    hours_salary = round(hourly_payment * hours_worked, 2)
    coefficient = (hours_salary * coefficient) - hours_salary
    sum_hours_coefficient = hours_salary + coefficient
    premium_percent = aht + flr + gok
    if position == "specialist":
        tests = 5 if tests == "yes" else 0
        premium_percent += tests + client_rating
    else:
        premium_percent += sl
    premium_salary = round(hours_salary * (premium_percent / 100), 2)
    salary_sum = round(sum_hours_coefficient + premium_salary, 2)

    tax = salary_sum * 0.13
    sum_after_tax = salary_sum - tax
    salary = {
        "hours_salary": hours_salary,
        "coefficient": coefficient,
        "sum_hours_coefficient": sum_hours_coefficient,
        "premium_percent": premium_percent,
        "premium_salary": premium_salary,
        "salary_sum": salary_sum,
        "tax": tax,
        "sum_after_tax": sum_after_tax,
    }
    return salary
