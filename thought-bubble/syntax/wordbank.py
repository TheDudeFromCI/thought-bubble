import random


class WordBank:
    def __init__(self):
        self.words = []

    def add_word(self, word: str, constituent: str):
        self.words.append({'word': word, 'type': constituent})

    def random_word(self, constituent: str) -> str:
        words = []
        for word in self.words:
            if word['type'] == constituent:
                words.append(word['word'])

        count = len(words)
        if count == 0:
            return None

        return words[random.randrange(count)]
