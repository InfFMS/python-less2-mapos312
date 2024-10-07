def a(x1, y1, x2, y2):
    return abs(x2 - x1) == abs(y2 - y1)
x1, y1, x2, y2 = map(int, input("Введите координаты клеток (x1 y1 x2 y2): ").split())
if a(x1, y1, x2, y2):
    print("YES")
else:
    print("NO")
