def do_twice(f,value):
    f(value)
    f(value)
      
def print_twice(stuff):
    print(stuff)
    
do_twice(print_twice,'dummy')