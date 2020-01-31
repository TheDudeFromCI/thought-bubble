from syntax.syntaxtree import SyntaxTree
from syntax.wordbank import WordBank
from config import loader
from syntax import builder

if __name__ == '__main__':
    tree = SyntaxTree()
    loader.load_rules('rules.config', tree)

    bank = WordBank()
    loader.load_words('words.csv', bank)

    print(builder.build_sentence(tree, bank, 'S'))
