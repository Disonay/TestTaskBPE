from task1.util import wrapped_bin


class Result:
    """
    Store input number, number after byte replacement and the binary representation of these numbers
    """
    def __init__(self, old_number: int, new_number: int):
        self.old_number = old_number
        self.new_number = new_number
        self.old_number_bin = wrapped_bin(old_number)
        self.new_number_bin = wrapped_bin(new_number)

    def __str__(self) -> str:
        return str(self.__dict__)
