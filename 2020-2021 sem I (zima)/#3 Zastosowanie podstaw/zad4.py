# Created by Marcin "Cozoob" Kozub 03.08.2021
import nltk, string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.porter import PorterStemmer

# nltk.download("stopwords")  # first time, then comment out / remove
# nltk.download("punkt")    # first time, then comment out / remove

def Bag_Of_Words(name_of_file):
    # I change the type to be a set because of in function (It works faster with sets).
    english_stop_words = set(stopwords.words("english"))
    # print(english_stop_words)
    stemmer = PorterStemmer()

    with open(name_of_file, "r") as file:
        dicitionary = {}
        for line in file:
            line.strip().isalnum()
            # I can do this since the words of the length 2 or less are not considered.
            if len(line) < 3:
                continue

            line = line.lower()
            # print(line, end="")

            line = line.split()
            # print(line)
            for word in line:
                if not word in english_stop_words:
                    stem_word = stemmer.stem(word)
                    if len(stem_word) < 3:
                        continue
                    dicitionary[stem_word] = dicitionary.get(stem_word, 0) + 1

            # print(line)
            # print()

        # print(dicitionary)

    return dicitionary


    # text = text.lower()
    # words = word_tokenize(text)
    # print(words)
    # stemmer = PorterStemmer()
    # word_stem = stemmer.stem("realization")
    # print(word_stem)
    # punctuations = string.punctuation
    # print(punctuations)






if __name__ == '__main__':
    print(Bag_Of_Words("texts.txt"))
