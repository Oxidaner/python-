def fib(n):
    if (n == 1 or n == 2):
        return 1
    return fib(n - 1) + fib(n - 2)


for i in range(1, 21):
    print(str(fib(i)).rjust(5, ' '), end=' ')
    if i % 10 == 0:
        print()
