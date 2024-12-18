def f(palindrome):
    test =''
    for i in palindrome:
        test = i + test
    if palindrome == test:
        return True
    else: 
        return False
    
palindrome = input("Enter word: ")
print(f'{palindrome} is palindrome? {f(palindrome)}')