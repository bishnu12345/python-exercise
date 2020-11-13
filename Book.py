import pymysql


class Book():
    def __init__(self):
        self.db = pymysql.connect('localhost', 'root', '', 'books')
        self.cursor = self.db.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print("ERRRO IN QUERY-------->"+str(e))

    # def update(self):
    #     self.dbconnection()
    #
    # def viewAll(self,query):
    #     cursor = self.db.cursor()
    #     cursor.execute(query)
    #     results = cursor.fetchall()
    #     return results


def display_menu():
    print("1.INSERT")
    print("2.UPDATE")
    print("3.VIEW ALL")
    print("4.DELETE")
    print("5.EXIT")


display_menu()

book1 = Book
user_choice = int(input('Enter option no: '))
try:
    while user_choice != 5:
        if user_choice == 1:
            book_name = input('Enter Book name ')
            author_name = input('Enter Author name ')
            price = input('Enter Book price ')
            sql = "INSERT into books (book_name, author, price) values ('{}','{}', {})".format(book_name,author_name,price)
            book1.insert(sql)
            break
        # elif user_choice == 2:
        #     pass
        # elif user_choice == 3:
        #     sql = 'SELECT * from books'
        #     book1.viewAll(sql)
        #     for r in range:
        #         print('{} {} {}'.format())


except Exception as e:
    print('ERROR------------>'+str(e))
