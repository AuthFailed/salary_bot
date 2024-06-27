async def salary_with_percents(
    position: str,
    hourly_payment: int,
    hours_worked: int,
    aht: int,
    flr: int,
    gok: int,
    client_rating: int = 0,
    tests: str = 0,
    sl: int = 0,
):
    hours_salary = round(hourly_payment * hours_worked, 2)
    premium_percent = aht + flr + gok
    if position == "specialist":
        tests = 5 if tests == "yes" else 0
        premium_percent += tests + client_rating
    else:
        premium_percent += sl
    premium_salary = round(hours_salary * (premium_percent / 100), 2)
    salary_sum = round(hours_salary + premium_salary, 2)

    salary = {
        "hours_salary": hours_salary,
        "premium_percent": premium_percent,
        "premium_salary": premium_salary,
        "salary_sum": salary_sum,
    }
    return salary
