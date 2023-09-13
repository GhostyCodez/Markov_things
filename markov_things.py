import string
import random

"The big red ball"
markov_dict = {}
user_in = input('Enter Words: ')
words = user_in.split()
for idx, word in enumerate(words[:-1]):
    current_word = word.lower().strip(string.punctuation)
    next_word = words[idx+1].lower().strip(string.punctuation)
    if current_word in markov_dict:
        markov_dict[current_word].append(next_word)
    else:
        markov_dict[current_word] = [next_word]
print(markov_dict)
seed = input('Enter seed word: ')
counter = 0
output = seed
while seed in markov_dict:
    seed = random.choice(markov_dict[seed])
    output += ' '+ seed
    counter += 1
    if counter == 20:
        break
print(output)