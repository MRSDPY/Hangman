import pandas as pd
import random as rd

dataset = pd.read_json("word_list.json", typ="Series")
word_data = dataset.index


def get_word():
    word = word_data[rd.randint(0, len(dataset))]
    return word
