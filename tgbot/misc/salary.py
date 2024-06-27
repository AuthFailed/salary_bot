import json


premium = {
    "flr": {
        103: 30,
        102: 25,
        101: 21,
        100: 18,
        95: 13,
    },
    "client_rating": {},
}


async def count_salary_with_numbers(
    # @TODO дописать расчет по цифрам
    hourly_payment: int,
    hours_worked: int,
    aht: int,
    flr: float,
    gok: int,
    client_rating: float,
    client_response: float,
    direction: str,
    position: str,
):

    salary = hourly_payment * hours_worked

    positions = json.load("normatives.json")

    if aht >= positions[direction][position]["aht"]:
        pass


async def count_salary_with_percents(
    hourly_payment: int,
    hours_worked: int,
    aht: int,
    flr: int,
    gok: int,
    client_rating: int,
):

    hours_salary = round(hourly_payment * hours_worked, 2)

    premium_percent = aht + flr + gok + client_rating

    premium_salary = round(hours_salary * (premium_percent / 100), 2)

    salary_sum = round(hours_salary + premium_salary, 2)

    salary = {
        "hours_salary": hours_salary,
        "premium_percent": premium_percent,
        "premium_salary": premium_salary,
        "salary_sum": salary_sum,
    }
    return salary
