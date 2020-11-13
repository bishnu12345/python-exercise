import pymysql


class Books:

    def __init__(self):
        self.db = pymysql.connect('localhost', 'root', '', 'books')
        self.cursor = self.db.cursor()


def insert(book_name, author, book_price):
    sql = "INSERT into books (book_name, author, price) values ('{}','{}', {})".format(book_name, author, book_price)




def display_menu():
    print("1.INSERT")
    print("2.UPDATE")
    print("3.VIEW ALL")
    print("4.DELETE")
    print("5.EXIT")


book1 = Books
display_menu()
user_choice = int(input('Enter option no: '))
try:
    while user_choice != 5:
        if user_choice == 1:
            book_name = input('Enter Book name ')
            author_name = input('Enter Author name ')
            price = input('Enter Book price ')
            book1.insert(book_name, author_name, price)

            break
except Exception as e:
    print('ERROR-------->'+str(e))
