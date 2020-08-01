def sol(n):
    return 1 if n <= 1 else n * sol(n - 1)


num = int(input())

print(sol(num))
