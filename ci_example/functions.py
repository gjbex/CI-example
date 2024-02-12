def fac(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n*fac(n - 1)
    else:
        raise ValueError('n must be positive')
