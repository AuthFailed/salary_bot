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
    acknowledgments: int = 0,
    mentoring_type: str = "",
    mentoring_days: float = 0,
):
    hours_salary = round(hourly_payment * hours_worked, 2)
    coefficient = round((hours_salary * coefficient) - hours_salary, 2)
    sum_hours_coefficient = hours_salary + coefficient
    premium_percent = aht + flr + gok
    if position == "specialist":
        tests = 5 if tests == "yes" else 0
        premium_percent += tests + client_rating + acknowledgments
        if mentoring_type != "":
            if mentoring_type == "3d":
                mentoring = mentoring_days * 0.5
            elif mentoring_type == "main":
                mentoring = mentoring_days * 1
            else:
                mentoring = mentoring_days * 1.5
            premium_percent += mentoring
    else:
        premium_percent += sl
    premium_salary = round(hours_salary * (premium_percent / 100), 2)
    salary_sum = round(sum_hours_coefficient + premium_salary, 2)

    tax = round(salary_sum * 0.13, 2)
    sum_after_tax = round(salary_sum - tax, 2)
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


async def vacation_pay(
    total_year_salary: float,
    vacation_days_count: int = 14,
    calendar_days_in_period: float = 351.6,
):
    vacation_pay = round(
        total_year_salary / calendar_days_in_period * vacation_days_count, 2
    )
    return vacation_pay
