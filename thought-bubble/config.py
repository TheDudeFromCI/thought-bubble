import csv


def load_words(file, wordbank):
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            wordbank.add_word(row[0], row[1])


def add_rule(rule, list):
    for e in rule:
        if e.startswith('('):
            return

    if rule not in list:
        list.append(rule)


def parse_rules(pre, rules, list):
    if rules[0].startswith('('):
        if len(rules) > 1:
            parse_rules(pre, rules[1:], list)
            parse_rules(pre + [rules[0][1:-1]], rules[1:], list)

        add_rule(pre + rules[1:], list)
        add_rule(pre + [rules[0][1:-1]] + rules[1:], list)
    else:
        if len(rules) > 1:
            parse_rules(pre + [rules[0]], rules[1:], list)

        add_rule(pre + rules, list)


def load_rules(file, tree):
    f = open(file, "r")
    for line in f.readlines():
        if line.isspace() or len(line) == 0 or line.startswith("#"):
            continue

        arrowIndex = line.index('->')
        con = line[:arrowIndex].strip()
        rules = line[arrowIndex + 3:].split(" ")
        rules = [r.strip() for r in rules]

        ruleList = []
        parse_rules([], rules, ruleList)

        for rule in ruleList:
            tree.add_rule(con, rule)
