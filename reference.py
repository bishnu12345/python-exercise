def display_name(name):
    print(name)


# Referencing through variables
copy_display_name = display_name

copy_display_name('Apoorba')
# copy_display_name is also referring to the same function display_name()


# Passing function as argument

def first_name(last_name_copy):
    print('Anil')
    print(last_name_copy.__name__)
    last_name_copy()


def last_name():
    print('Shrestha')


first_name(last_name)


def number(num):
    print(num)

    def is_positive():
        if num>0:
            print('Positive')
        else:
            print('Negative')
    is_positive()


number(10)

