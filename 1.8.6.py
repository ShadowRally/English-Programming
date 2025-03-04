Age1=int (input ("How old are you?: "))

def my_function(Age1):
    retstr=""
    if Age1 >= 18:
        retstr= "You are an adult"
    
    else:
        retstr= "You are not an adult so NO drinking for you!"
    return retstr

print (my_function(Age1))