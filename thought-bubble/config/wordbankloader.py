import csv


def load_words(file, wordbank):
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            wordbank.add_word(row[0], row[1])
