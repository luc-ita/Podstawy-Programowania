def f(dice):
    max_dices = ''
    dice_1 = 0
    dice_2 = 0
    dice_3 = 0
    dice_4 = 0
    dice_5 = 0
    dice_6 = 0
    
    
    for i in dice:
        if i == '1':
            dice_1 += 1
        elif i == '2':
            dice_2 += 1
        elif i == '3':
            dice_3 += 1
        elif i == '4':
            dice_4 += 1
        elif i == '5':
            dice_5 += 1
        elif i == '6':
            dice_6 += 1

    result = max(dice_1, dice_2, dice_3, dice_4, dice_5, dice_6)

    if dice_1 == result:
        max_dices += '1' + ' '
    if dice_2 == result:
        max_dices += '2' + ' '
    if dice_3 == result:
        max_dices += '3' + ' '
    if dice_4 == result:
        max_dices += '4' + ' '
    if dice_5 == result:
        max_dices += '5' + ' '
    if dice_6 == result:
        max_dices += '6' + ' '
    return max_dices

dice = input()
print(f(dice))