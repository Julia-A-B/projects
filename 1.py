def fibonacci(n):
    i = 0
    b = 0
    c = 1
    if n == 0:
        a = b
    elif n == 1:
        a = c
    else:
        for i in range(n - 1):
            a = b + c
            b = c
            c = a
            i = i + 1

    return a
