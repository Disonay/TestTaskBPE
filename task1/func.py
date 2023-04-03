from objects import Result


def change_bytes(number: int) -> Result:
    """
    Swap the bytes of a number

    :param number: positive integer 2-byte number
    :return: Result object
    """
    right_part = (number & 255) << 8
    left_part = (number & 65280) >> 8

    return Result(number, right_part | left_part)


if __name__ == "__main__":
    print(change_bytes(65000))
