from syntaxtree import SyntaxTree
from wordbank import WordBank
import config
import builder

if __name__ == '__main__':
    tree = SyntaxTree()
    config.load_rules('rules.config', tree)

    bank = WordBank()
    config.load_words('words.csv', bank)

    print(builder.build_sentence(tree, bank, 'S'))
