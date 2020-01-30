words = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
hg = {}


def histogram(ls):
    for i in ls:
        hg[i] = hg.get(i, 0) + 1
    return hg

    # for (i) in histogram:
    #     print(i + ": " + str(histogram.get(i)))


def unique():
    # unique_words = []
    # for i in histogram:
    #     if i not in unique_words:
    #         unique_words.append(i)
    return len(list(hg.keys()))


def frequency(word, hist):
    if word in list(hg.keys()):
        return hg.get(word)


if __name__ == '__main__':
    print(histogram(words))
    print(unique())
    print(frequency("one", hg))
