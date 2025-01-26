import queue

INPUT = 18


def convert_to_binary(decimal):
    stack = queue.LifoQueue()
    dec_to_bin(decimal, stack)

    output = list()
    while not stack.empty():
        bin_value = stack.get()
        output.append(bin_value)

    return ''.join(map(str, output))


def dec_to_bin(dec: int, stack: queue.LifoQueue):
    if dec == 0:
        stack.put(0)
    elif dec == 1:
        stack.put(1)
    else:
        stack.put(dec % 2)
        return dec_to_bin(dec // 2, stack)


def main():
    print('Natural number: ', INPUT)
    print('Binary number: ', convert_to_binary(INPUT))


if __name__ == '__main__':
    main()