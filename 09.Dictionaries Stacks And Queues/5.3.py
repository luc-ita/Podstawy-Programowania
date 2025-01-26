translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}



word = input("Enter an English word: ").strip()
translation = translations.get(word.lower(), "Translation unavailable")
print(f"The Polish translation is: {translation}")
