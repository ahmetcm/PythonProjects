def shift_reduce(input_string):
    grammar = [
        ("E", "E+T"),
        ("E", "T"),
        ("T", "T*F"),
        ("T", "F"),
        ("F", "(E)"),
        ("F", "i")
    ]

    parsing_table = {
        (0, 'i'): 's5', (0, '('): 's4', (0, 'E'): 1, (0, 'T'): 2, (0, 'F'): 3,
        (1, '+'): 's6', (1, '$'): 'acc',
        (2, '+'): 'r2', (2, '*'): 's7', (2, ')'): 'r2', (2, '$'): 'r2',
        (3, '+'): 'r4', (3, '*'): 'r4', (3, ')'): 'r4', (3, '$'): 'r4',
        (4, 'i'): 's5', (4, '('): 's4', (4, 'E'): 8, (4, 'T'): 2, (4, 'F'): 3,
        (5, '+'): 'r6', (5, '*'): 'r6', (5, ')'): 'r6', (5, '$'): 'r6',
        (6, 'i'): 's5', (6, '('): 's4', (6, 'T'): 9, (6, 'F'): 3,
        (7, 'i'): 's5', (7, '('): 's4', (7, 'F'): 10,
        (8, '+'): 's6', (8, ')'): 's11',
        (9, '+'): 'r1', (9, '*'): 's7', (9, ')'): 'r1', (9, '$'): 'r1',
        (10, '+'): 'r3', (10, '*'): 'r3', (10, ')'): 'r3', (10, '$'): 'r3',
        (11, '+'): 'r5', (11, '*'): 'r5', (11, ')'): 'r5', (11, '$'): 'r5',
}

    stack = [0]
    input_string += "$"
    pointer = 0

    while True:
        current_state = stack[-1]
        current_symbol = input_string[pointer]

        action = parsing_table.get((current_state, current_symbol))

        if action is None:
            return "INVALID string entered. SYNTAX ERROR!"

        if action == 'acc':
            return "VALID string entered. ACCEPTED!"

        if action.startswith('s'):
            stack.append(current_symbol)
            stack.append(int(action[1:]))
            pointer += 1

        elif action.startswith('r'):

            rule_index = int(action[1:]) - 1

            _, rhs = grammar[rule_index]

            for _ in range(2 * len(rhs)):

                stack.pop()

            top_state = stack[-1]
            stack.append(grammar[rule_index][0])

            next_state = parsing_table.get((top_state, stack[-1]))

            if next_state is None:
                return "INVALID string entered. SYNTAX ERROR!"

            stack.append(int(next_state))


input_string = input("Enter your string:\n")

if "d" in input_string:
    input_string = input_string.replace('d', '')

result = shift_reduce(input_string)
print(result)
