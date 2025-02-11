import math
print("You are gonna write a number and then ad a VAT to it so please write some numbers")

math1=int(input("Write a number: "))
math2=int(input("Write a VAT: "))
math3=(math2/100)+1
def my_function(math1,math3):
  return (math1*math3)

print (my_function(math1,math3))