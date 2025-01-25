import re

text = input("Enter your text: ")

vowel_pattern = r'[aeiouyAEIOUY]'

vowels = re.findall(vowel_pattern, text)
num_vowels = len(vowels)

print(f"Number of vowels in the text: {num_vowels}")
