def frequency():
    words = ("one", "fish", "two", "fish", "red", "fish", "blue", "fish")
    histogram = {}

    for i in words:
        histogram[i] = histogram.get(i, 0) + 1
    print(histogram)

    for (i) in histogram:
        print(i + ": " + str(histogram.get(i)))


if __name__ == '__main__':
    frequency()
