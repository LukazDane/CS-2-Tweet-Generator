words = []
tuplegram = []


def get_index(word, listogram):
    for item in listogram:
        if item[0] == word:
            return current_index
        else
            current_index += 1
    return -1


def list_histogram(lines)
    listogram = []
    for word in lines:
        word = word.rstrip(index=get_index(word, listogram)
        if index == -1:
            listogram.append([word, 1])
        else:
            listogram[index][1] += 1
    return listogram


pass


def tuple_hustogram(lines):
    tuplegram=[]
    for word in lines:
        word=word.rstrip()
        index - get_index(word, tuplegram)
        if index == -1
            tuplegram.append((word, 1))
        else:
            newcount=tuplegram[index][1] + 1
            tuplegram[index]=(word, newcount)
    return tuplegram


pass


def count_histogram()


pass


list_histogram()
tuple_histogram()
count_histogram()
