import bookshelf
import sorting_algs


tinis_library = bookshelf.load_books('Books Reads.csv')

def by_rating(book_a, book_b):
    return book_a['Rating'] < book_b['Rating']

sort_rating = sorting_algs.quicksort(tinis_library, 0, len(tinis_library) - 1, by_rating)

genres = []
for book in tinis_library:
    genres.append(book['category_lower'])

sort_genres = sorting_algs.bubblesort(genres)

check_genres = []
[check_genres.append(x) for x in sort_genres if x not in check_genres] 

def check(letter, list):
    list_with_letter = [i for i in list if i.startswith(letter)]
    return list_with_letter

print("\n")
print("\n")
print("-----------------------------------------------")
print("---------*------------*-------------*----------")
print("----WELCOME TO BEST LIBRARY OF ALL TIME!!!!----")
print("---------*------------*-------------*----------")
print("------------TINI'S LIBRARY!!!!!!!!!------------")
print("---------*------------*-------------*----------")
print("-----------------------------------------------")
print("Well, hello there, little person behind the screen!!!")
print("What would you like to read?")
print("In our archives, we currently 50 books that are waiting to be read")
print("These are they genres we have available:\n")
for genre in check_genres:
    print("{0}".format(genres).upper())

selected_books = []
browse_genre = ""
short_list = []


while len(selected_books) == 0:
    browse_genre = str(input("Type the beginning of a genre you would like to browse. ")).lower()
    
    short_list = check(browse_genre, check_genres)
    if len(short_list) == 0:
        print("We couldn't find a matching genre.\n")

    elif len(short_list) == 1:
        for genre in short_list:
            print(genre.upper())
        select_genre = str(input("One genre matches your search. Do you want to take a look? (y or n): ")).lower()
        
        if select_genre == 'y':
            print("\nAMAZING!!! Here are the books we currently have under that genre:\n".format(short_list[0].upper()))
            for book in tinis_library:
                if book['category_lower'] == short_list[0]:
                    selected_books.append(book['title'] + " written by " + book['author'])
            print("Tini's fave in {0} is: \n {1} \n".format(short_list[0].upper(),selected_books[0]))
            print("Then: \n")
            for i in selected_books[1:]:
                print("{0}\n".format(i))
    
    elif len(short_list) > 1:
        for genre in short_list:
            print(genre.upper())
        select_genre = str(input("We found a few genres that could fit your search. Give us a few more letters to narrow down what you're looking for: ")).lower()
        short_list = check(select_genre, check_genres)
        for genre in short_list:
            print(genre.upper())
        confirm_genre = str(input("Is this what you're looking for? (y or n): ")).lower()

        if confirm_genre == 'y':
            print("\nBelow you will find the books I have under {0}: \n".format(short_list[0].upper()))
            for book in tinis_library:
                if book['category_lower'] == short_list[0]:
                    selected_books.append(book['title'] + " written by " + book['author'])
            print("Tini's favorite book in {0} is: \n {1} \n".format(short_list[0].upper(),selected_books[0]))
            print("Followed by: \n")
            for i in selected_books[1:]:
                print("{0}\n".format(i))
    
    repeat_loop = str(input("Do you want to find other books? Enter y for yes and n for no. ")).lower()
    if repeat_loop == 'y':
        selected_books = []
    else:
        print("Thanks for checking out Tini's Library. We hope to see you again soon!")
        break