import queue

INPUT = 'Define a function that takes a string'


def reverse_string(input_str):
    stack = queue.LifoQueue()
    for l in input_str:
        stack.put(l)

    output_str = ''
    while not stack.empty():
        output_str = output_str + stack.get()

    return output_str


print(f'Original string: {INPUT}')
print(f'Reversed string: {reverse_string(INPUT)}')
    
