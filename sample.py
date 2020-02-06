import random
import sys

# words = sys.argv[1:]
words = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
histogram = {'cats': 3, 'dogs': 4, 'rabbits': 2, 'turtles': 1}

hg = {'cats': 3, 'dogs': 4, 'rabbits': 2, 'turtles': 1}


def sample(histogram):
    tokens = sum([count for word, count in histogram.items()])
    dart = random.randint(1, tokens)
    fence = 0
    for word, count in histogram.items():
        fence += count
        if fence >= dart:
            return word


print(sample(histogram))

""" 
import random
from random import randint
text = 'one fish two fish red fish blue fish'
word_counts = {'one': 1, 'fish': 4, 'two': 1,
               'red': 1, 'blue': 1}
               
def sample_by_frequency(histogram):
    new_ls = []              

    # TODO: select a word based on frequency
    #how can we sample words using observed frequencies?
    #call randint to give us a random index to help us select a word
    for k in word_counts:
      new_ls.append(random.choice([k for k in word_counts for x in range(word_counts[k])]))
    return new_ls
print(sample_by_frequency(word_counts))

#for key in word_counts 
#append random choice
# k for each key(5) for x in ramge of word_counts*value of K

#start = 0
#for word in count of histogram.items():
  #end = start + 
  # if 
    # return word
  # else 
"""
