import math

def ToPercentage(val):
  val=val*100
  val=int(round(val))
  return (val)

while True:
    try:
        math1=float(input("Write a decimal: "))
        break
    except ValueError:
       print("Weirdo! Write right things!")
print (ToPercentage(math1))