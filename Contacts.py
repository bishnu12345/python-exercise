import pymysql


class Database:
    def __init__(self):
        self.connection = pymysql.connect('localhost', 'root', '', 'contact')
        self.cursor = self.connection.cursor()

    def execute(self, query, *args):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print('EXECUTION ERROR------->'+str(e))
            self.connection.rollback()


def insert(name, email, contact_no):
    db = Database()
    sql = "Insert into contacts values('{}', '{}', {})".format(name, email, contact_no)
    Database.execute(db, sql, (name, email, contact_no))


def update(email):
    db = Database()
    sql = "Update contacts set values = "
    Database.execute(db, sql, )


def viewall():
    db = Database()
    sql = "SELECT * from contacts"
    Database.execute(db, sql)
    results = db.cursor.fetchall()
    return results


def delete(email):
    db = Database()
    sql = "DELETE from contacts where email={}".format(email)
    Database.execute(db, sql, email)


def display_menu():
    print("****WELCOME TO CONTACT APPLICATION****")
    print("1.INSERT CONTACT")
    print("2.UPDATE CONTACT")
    print("3.VIEW ALL CONTACTS")
    print("4.DELETE CONTACT")
    print("5.EXIT")


display_menu()
user_choice = int(input('Enter choice: '))
while user_choice != 5:
    if user_choice == 1:
        name = input('Enter name: ')
        email = input('Enter email: ')
        contact_no = int(input('Enter contact no: '))
        insert(name, email, contact_no)
        break
    elif user_choice == 2:
        user_email = input('Enter email of the contact to update: ')

        break
    elif user_choice == 3:
        results = viewall()
        print('Id-----Name------Email-------Contact No')
        for i in results:
            print('{}------{}------{}-----{}'.format(i[0], i[1], i[2], i[3]))
        break
    elif user_choice == 4:
        delete_email = input('Enter email of the contact to delete: ')
        delete(delete_email)
        break




