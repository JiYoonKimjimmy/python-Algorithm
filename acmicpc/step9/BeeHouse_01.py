def sol(t, room, start):
    end = start + (room * 6)
    if t < end:
        return room + 1
    else:
        while t >= end:
            end = start + (room * 6)
            if start <= t & t < end:
                return room + 1
            else:
                start = end
                room += 1
                sol(t, room, start)


n = int(input())

if n == 1:
    print(1)
else:
    print(sol(n, 1, 2))
