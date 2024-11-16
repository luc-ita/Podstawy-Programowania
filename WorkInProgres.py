###
# 6.10
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(movie.upper())

# print title in small letters
print(movie.casefold())

# print how many times the vowel "e" appears in the title
print(movie.count("e"), ' of e')

# print where in the text is the word "Lord"
print('Lord is on', movie.find("Lord"))

# print where in the text is the word "dragon"
if (movie.find("dragon")) == -1:
    print('There is no dragon in this title')
else:
    print('dragon is on', movie.find("dragon"))