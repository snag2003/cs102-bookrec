import csv

def load_books(filename):
  bookshelf = []
  with open(filename) as file:
      shelf = csv.DictReader(file)
      for book in shelf:
          # add your code here
          book['author_lower'] = book['author'].lower()
          book['title_lower'] = book['title'].lower()
          book['category_lower'] = book['category'].lower()
          book['rating']
          bookshelf.append(book)
  return bookshelf

print(load_books('Books Reads.csv'))