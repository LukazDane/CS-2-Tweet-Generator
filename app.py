from flask import Flask
from frequency import histogram
from sample import sample
from markov import MarkovChain
app = Flask(__name__)


@app.route('/')
def gen_word():
    my_file = open("./words.txt", "r")
    lines = my_file.readlines()
    my_histogram = histogram(lines)

    sentence = ""
    num_words = 10
    # for i in range(num_words):
    #     word = sample(my_histogram)
    #     sentence += " " + word
    markovchain = MarkovChain(lines)
    sentence = markovchain.walk(num_words)
    return sentence


if __name__ == '__main__':
    app.run()
