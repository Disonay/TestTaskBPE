from typing import Iterator


def count_symbols(data: str | Iterator[str]) -> dict:
    """
    Count how many times which characters occur in the string or strings.

    :param data: string or iterator of strings
    :return: dict with result
    """
    result = {}
    for line in data:
        for symbol in line:
            number = result.get(symbol)
            if number:
                result.update({symbol: number + 1})
            else:
                result[symbol] = 1

    return result
