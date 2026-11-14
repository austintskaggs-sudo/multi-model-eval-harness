def average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += i
    return total / len(numbers)


print(average([10, 20, 30]))
print(average([]))
