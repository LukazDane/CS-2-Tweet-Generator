words = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
histogram = {}


def frequency():
    for i in words:
        histogram[i] = histogram.get(i, 0) + 1
    return histogram

    # for (i) in histogram:
    #     print(i + ": " + str(histogram.get(i)))


def unique():
    # unique_words = []
    # for i in histogram:
    #     if i not in unique_words:
    #         unique_words.append(i)
    return list(histogram.keys())


if __name__ == '__main__':
    print(frequency())
    print(unique())
