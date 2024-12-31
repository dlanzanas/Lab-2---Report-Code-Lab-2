import random

def getWords(filename):
    with open(filename, 'r') as file:
        return tuple(word.strip() for word in file.readlines())

articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')

def sentence():
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    while True:
        try:
            number = int(input("Enter the number of sentences: "))
            if number <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    for _ in range(number):
        print(sentence())

if __name__ == "__main__":
    main()
