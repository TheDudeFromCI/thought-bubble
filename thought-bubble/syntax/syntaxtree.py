class SyntaxTree:
    """
    The syntax tree is used to define the rules for how a sentence should be structured.
    It consists of a set of rules for what constituents exist and how they can be broken
    down into smaller constituents, if possible.
    """

    def __init__(self):
        self.rules = []
        self.constituents = []

    def add_constituent(self, constituent: str):
        """
        Adds a new constituent type to this syntax tree. If the given constituent is
        already in this tree, nothing happens.
        """

        if constituent not in self.constituents:
            self.constituents.append(constituent)

    def add_rule(rule, constituent: str, subconstituents: list(str)):
        """
        Adds a new rule to this syntax tree. The given constituent and subconstituents
        are added to the tree if they are not already present.

        A rule is used to define how a constituent should be broken down into other
        constituents when forming a sentence. A word is selected when a constituent
        cannot be broken down any further.
        """

        self.add_constituent(constituent)

        for sub in subconstituents:
            self.add_constituent(sub)

        self.rules.append(constituent, subconstituents)
