from syntax import syntaxtree

if __name__ == '__main__':
    tree = SyntaxTree()

    tree.add_constituent('S')   # Sentence
    tree.add_constituent('NP')  # Noun Phrase
    tree.add_constituent('VP')  # Verb Phrase
    tree.add_constituent('PP')  # Prepositional Phrase
    tree.add_constituent('N')   # Noun
    tree.add_constituent('V')   # Verb
    tree.add_constituent('C')   # Conjuction
    tree.add_constituent('Ad')  # Adjective
    tree.add_constituent('D')   # Determiner
    tree.add_constituent('P')   # Preposition
    tree.add_constituent('Au')  # Auxilary Verb

    tree.add_rule('S', ['NP', 'VP'])
    tree.add_rule('S', ['NP', 'Au', 'VP'])
    tree.add_rule('S', ['S', 'C', 'S'])

    tree.add_rule('NP', ['N'])
    tree.add_rule('NP', ['D', 'N'])
    tree.add_rule('NP', ['Ad', 'N'])
    tree.add_rule('NP', ['D', 'Ad', 'N'])
    tree.add_rule('NP', ['N', 'PP'])
    tree.add_rule('NP', ['D', 'N', 'PP'])
    tree.add_rule('NP', ['Ad', 'N', 'PP'])
    tree.add_rule('NP', ['D', 'Ad', 'N', 'PP'])
    tree.add_rule('NP', ['NP', 'C', 'NP'])

    tree.add_rule('PP', ['P'])
    tree.add_rule('PP', ['P', 'NP'])
    tree.add_rule('PP', ['PP', 'C', 'PP'])

    tree.add_rule('VP', ['V'])
    tree.add_rule('VP', ['V', 'NP'])
    tree.add_rule('VP', ['V', 'NP', 'PP'])
    tree.add_rule('VP', ['V', 'NP', 'PP', 'Ad'])
    tree.add_rule('VP', ['V', 'NP', 'Ad'])
    tree.add_rule('VP', ['V', 'PP'])
    tree.add_rule('VP', ['V', 'PP', 'Ad'])
    tree.add_rule('VP', ['V', 'Ad'])
    tree.add_rule('VP', ['VP', 'C', 'VP'])
