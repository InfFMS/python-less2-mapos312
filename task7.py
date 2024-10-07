N = int(input())
c=0
for b in range (2, N + 1):
    for a in range(2, b):
        if b % a == 0:
           c+=1
    if c == 0:
        print(b)
    c=0