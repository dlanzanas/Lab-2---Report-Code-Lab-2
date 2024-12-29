def median(numbers):
    if not numbers: 
        return 0
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:  
        return numbers[midpoint]
    else: 
        return (numbers[midpoint - 1] + numbers[midpoint]) / 2

def mode(numbers):
    if not numbers: 
        return 0
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_freq]
    if len(modes) == 1:
        return modes[0] 
    return modes  

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
