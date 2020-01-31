from syntaxtree import SyntaxTree
from wordbank import WordBank
import random

"""
This file contains the functions used to generate a sentence using the given syntax tree.
"""


def is_complete_sentence(sentence) -> bool:
    for e in sentence:
        if not e['is_word']:
            return False

    return True


def build_sentence(tree: SyntaxTree, wordBank: WordBank, default: str) -> str:
    sentence = [{'text': default, 'is_word': False}]

    while not is_complete_sentence(sentence):
        for x in range(len(sentence)):
            if sentence[x]['is_word']:
                continue

            con = sentence[x]['text']
            rules = tree.get_rules(con)

            if len(rules) == 0:
                sentence[x] = {'text': wordBank.random_word(
                    con), 'is_word': True}
                break

            rule = rules[random.randrange(len(rules))]
            rule = [{'text': r, 'is_word': False} for r in rule]

            sentence = sentence[:x] + rule + sentence[x + 1:]
            break

    out = ""

    for word in sentence:
        if len(out) != 0:
            out += " "

        out += word['text']

    return out
