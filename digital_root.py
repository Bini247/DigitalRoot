def digital_root(n):
    if n < 0:
        return -1
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n
