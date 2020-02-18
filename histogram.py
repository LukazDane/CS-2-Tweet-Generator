word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
histogram = {}


# def get_index(word, listogram):
#     for item in listogram:
#         if item[0] == word:
#             return current_index
#         else:
#             current_index += 1
#     return -1
def dictogram():
    for word in word_list:
        histogram[word] = histogram.get(word, 0) + 1
    return histogram


def list_histogram():
    new_word_list = []
    list_of_lists = []

    for word in word_list:
        if word in new_word_list:
            word_index = new_word_list.index(word)
            new_word_list[word_index + 1] += 1
        else:
            new_word_list.append(word)
            new_word_list.append(1)

    for x in range(0, len(new_word_list), 2):
        list_of_lists.append([new_word_list[x], new_word_list[x+1]])

    return list_of_lists


if __name__ == '__main__':
    print(dictogram())
    print(list_histogram())
