import csv

filename = 'books.csv'


def read_books(filename):
    books = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append(row)
    return books


def extract_unique_genre(books):
    return set([b['Genre'] for b in books])


def filter_books_by_genre(books, genre):
    return [book for book in books if book['Genre'] == genre]


def save_books_to_file(books, genre):
    genre_lowercased = genre.lower().replace(' ', '-')
    filename = f'books_{genre_lowercased}.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        for book in books:
            file.write(f"{book['Title']}, {book['Author']}, {book['Genre']}, {book['Year']}\n")
    return filename


def process_genre(books, genre):
    genre_books = filter_books_by_genre(books, genre)
    filename = save_books_to_file(genre_books, genre)
    print(f"Saved {len(genre_books)} books to {filename}")



books = read_books(filename)
genre = extract_unique_genre(books)

for g in genre:
    process_genre(books, g)
