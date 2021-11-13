# Generators
# generators are a type of iterables which can not be accesed using index but can be iterated
# through for loops
def countdown() :
    i = 5
    while i > 0 :
        yield i
        i -= 1
for i in countdown() :
    print(i)
# Finite generators into lists
def even(x) :
    for i in range(x) :
        if i%2 == 0 :
            yield i
print(list(even(10)))
# split generator
sent = "hello python world"

# Decorator , provide a way to extend the functionality of a func which we do not want to modify
# functions that modify other functions
def decor(func):
    def wrap() :
        print("##########")
        func()
        print("+++++++++++")
    return wrap
def print_tex() :
    print("shourya")

decorated = decor(print_tex)
decorated()

# we can decorate a function by pre pending a function with
# the decoration is taken from the above example
# replaces the 31 line of code
@decor
def print_word() :
    print("sHOURYA IS GREATEST OF ALL TIME ")
print_word()




