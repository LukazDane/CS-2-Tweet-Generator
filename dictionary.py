import random
from random import randint, choice
# shoud not need to use choice for this, review later
import sys

# f = open("words.txt", "r")
# words = f.readlines()
# f.close()


def random_words(words, num):
    list_words = []
    for i in range(num):
        rand_index = random.randint(0, len(words))
        list_words.append(choice(words))
    return ''.join(list_words).replace('\n', " ")
    # in line
    return ''.join(list_words)
    # new line after each word


if __name__ == '__main__':
    words = list(open("/usr/share/dict/words", "r"))
    print(random_words(words, int(sys.argv[1])))
