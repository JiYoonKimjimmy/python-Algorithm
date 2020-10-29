def shift(arr, n):
    arr.reverse()
    add_arr = []
    for _ in range(n):
        add_arr.append(arr.pop())
    arr.reverse()
    arr.extend(add_arr)
    print(arr)


shift([1, 2, 3, 4, 5, 6], 2)
