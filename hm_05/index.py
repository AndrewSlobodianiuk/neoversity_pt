import re


def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]

        if n == 0:
            return 0

        if n == 1:
            return 1

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci


get_fibonacci = caching_fibonacci()

# print(get_fibonacci(0))
# print(get_fibonacci(1))
# print(get_fibonacci(2))
# print(get_fibonacci(3))
# print(get_fibonacci(4))
# print(get_fibonacci(15))


def generator_numbers(text):
    pattern = r"(?<=\s)\d+\.\d+(?=\s)"

    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text, gen_amounts):
    return sum(gen_amounts(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")
