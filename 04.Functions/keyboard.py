def input_string(message):
    return str(input(message))

def input_integer(message):
    return int(input(message))

def input_real(message):
    return float(input(message))

def input_boolean(message):
    exe = input(message)
    if exe == 'y':
        return True
    elif exe == 'n':
        return False
