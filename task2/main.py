def identify_false_basket(N: int, w: int, d: int, P: int) -> int:
    """
    Find basket with fake coins

    :param N: number of baskets
    :param w: real coin weight
    :param d: the weight by which a fake coin differs
    :param P: the total weight of the selected coins.

    :return: basket number
    """
    sum_without_false = N * (N - 1) * w // 2
    basket_with_false = (sum_without_false - P) // d

    return basket_with_false if basket_with_false else N


if __name__ == "__main__":
    print(identify_false_basket(7, 2, 1, 39))
