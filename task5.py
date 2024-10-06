def find_numbers():
    results = []
    for n in range(10000, 100000):
        if n % 133 == 125 and n % 134 == 111:
            results.append(n)
    return results
numbers = find_numbers()
print(numbers)

