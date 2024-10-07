def a(a1, b1, a2, b2):
    start = max(a1, a2)
    end = min(b1, b2)
    if start < end:
        return (start, end)
    elif start == end:
        return (start,)
    else:
        return None
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a = a(a1, b1, a2, b2)
if a:
    if len(a) == 1:
        print(f"Общая точка: {a[0]}")
    else:
        print(f"Пересечение: [{a[0]}, {a[1]}]")
else:
    print("пустое множество")