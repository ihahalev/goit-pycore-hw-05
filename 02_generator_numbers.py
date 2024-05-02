import re
from decimal import Decimal
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[str, None, None]:
    filter_pattern = r" \d+\.\d+ "
    numbers: list[str] = re.findall(filter_pattern, text)
    for num in numbers:
        # for proper rounding
        amount = Decimal(num.strip())
        yield amount.quantize(Decimal('0.00'))

def sum_profit(text: str, func: Callable[[str], float]) -> float:
    sum = 0
    for num in func(text):
        sum += num
    return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")