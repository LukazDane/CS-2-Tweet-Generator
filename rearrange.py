import random
import sys

words = sys.argv[1:]

shuffled = []


def rearrange():
    for i in range(len(words)):
        rand_index = random.randint(0, len(words) - 1)
        shuffled.append(words[rand_index])


if __name__ == '__main__':
    word = rearrange()
    print(*words[0:])
    # print(*shuffled) #
