import random
import sys

words = sys.argv[1:]


def sample(ls):
    for i in ls:
        return [ls[random.randint(0, (len(ls)-1))]]


print(*sample(words))
