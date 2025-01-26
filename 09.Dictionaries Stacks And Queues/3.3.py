import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"  # brackets not correct
expression3 = "(2-3*4+(5/6)"  # brackets not correct

bracket_map = {
    '[': ']',
    '(': ')',
    '{': '}'
}


def brackets_ok(expression):
    brackets = queue.LifoQueue()
    for element in expression:
        if element in ['[', '(', '{']:
            brackets.put(element)
        elif element in [']', ')', '}']:
            opening_bracket = brackets.get()
            if not bracket_map[opening_bracket] == element:
                return False
    return brackets.empty()


for expression in [expression1, expression2, expression3]:
    if brackets_ok(expression):
        print(f'expression {expression} is valid')
    else:
        print(f'expression {expression} is invalid')