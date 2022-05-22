def zeros(n):
    z = 0
    i = 5
    while n>=i:
        z += n // i
        i *= 5
    return z