def sumatoria(n):
    a = 1
    b = 0
    den = 2
    s = 0
    k = 1
    for i in range(n):
        num = a + b
        s = s + (k) * (num/den)
        print(s)
        a = b
        b = num
        den *= 2
        k = (-1) * k
    return s

n = int(input(": "))
s = sumatoria(n)
print(s)