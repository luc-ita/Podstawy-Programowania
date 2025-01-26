import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put('King of Hearts \u2665')
cards.put('Queen of Diamonds \u2666')
cards.put('Jack of Spades \u2660')

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# removes and prints elements from the top of the stack
while not cards.empty():
    card = cards.get()
    print(card)

"""
Note the order of the printed elements.
The last added element is printed first.
"""

# solution
cards.put(2)
cards.put(3)
cards.put(7)
cards.put(4)
cards.put(1)
cards.put(9)
cards.put(8)


def sum_last_two_numbers(cards):
    numbers = [cards.get() for _ in range(2)]
    return sum(numbers)


def sum_all_numbers(cards):
    total = 0
    while not cards.empty():
        card = cards.get()
        total += card
    return total

print()
print('Sum of last two numbers:', sum_last_two_numbers(cards))
print('Sum of the rest:', sum_all_numbers(cards))