word = input("Enter a word: ")

score = 0 

for letter in word:
    
    if letter in 'aeioulnrst':
        score += 1
    elif letter in 'dg':
        score += 2
    elif letter in 'bcmp':
        score += 3
    elif letter in 'fhvwy':
        score += 4
    elif letter in 'k':
        score += 5
    elif letter in 'jx':
        score += 8
    elif letter in 'qz':
        score += 10
    elif letter in 'авеинорст':
        score += 1
    elif letter in 'дклмпу':
        score += 2
    elif letter in 'бгёья':
        score += 3
    elif letter in 'йы':
        score += 4
    elif letter in 'жзхцч':
        score += 5
    elif letter in 'шэю':
        score += 8
    elif letter in 'фщъ':
        score += 10

print(f'Cost of the word {word} is {score} points.')