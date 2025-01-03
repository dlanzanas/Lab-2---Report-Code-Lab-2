from collections import Counter

def median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_numbers[mid_index]
    return (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2

def mode(numbers):
    if not numbers:
        return 0
    frequency = Counter(numbers)
    max_freq = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_freq]
    return modes[0] if len(modes) == 1 else modes

def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    numbers = [1, 2, 2, 3, 4]
    
    # stats
    print("Numbers:", numbers)
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))
    print("Mean:", mean(numbers))

if __name__ == "__main__":
    main()
