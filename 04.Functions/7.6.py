import card_hide
while True:
    number = input()
    if len(number) == 16:
        break
print(number, card_hide.main(number))