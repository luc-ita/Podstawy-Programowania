def main(card_number):
    mask= ''
    count = 0
    for i in card_number:
        count += 1
        if count >= 3 and count <= 14:
            mask += '*'
        else:
            mask += i
    return mask
