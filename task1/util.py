def wrapped_bin(number: int):
    old_bin = bin(number)[2:]
    if len(old_bin) != 16:
        old_bin = "0"*(16-len(old_bin)) + old_bin

    return old_bin[:8] + " " + old_bin[8:]
