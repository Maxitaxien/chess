with open('rules.txt', 'r') as rules:
    instructions_text = ''.join([(line) for line in rules.readlines()])

    print(instructions_text)