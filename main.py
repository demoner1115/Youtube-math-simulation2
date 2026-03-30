n = 1
for i in range(1000):
    b = n * n * n
    a = [int(x) for x in str(b)]
    c = sum(a)
    if c == n:
        print(n)
    n += 1
