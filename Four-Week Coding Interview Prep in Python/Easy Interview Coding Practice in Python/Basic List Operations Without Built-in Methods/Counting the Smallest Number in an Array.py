def count_min(numbers):
    if not numbers:
        return 0

    smallest = numbers[0]
    amount = 1

    for index in range(1, len(numbers)):
        if numbers[index] < smallest:
            smallest = numbers[index]
            amount = 1
        elif numbers[index] == smallest:
            amount += 1

    return amount
