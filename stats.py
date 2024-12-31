def median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    midpoint = len(sorted_numbers) // 2
    if len(sorted_numbers) % 2 == 1:
        return sorted_numbers[midpoint]
    else:
        return (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2

def mode(numbers):
    if not numbers:
        return 0
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_freq]
    return modes[0] if len(modes) == 1 else modes

def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    numbers = [1, 2, 2, 3, 4]

    print("Numbers:", numbers)
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))
    print("Mean:", mean(numbers))

if __name__ == "__main__":
    main()
