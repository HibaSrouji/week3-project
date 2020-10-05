## the first function
'''
Week2 paper Airplane 
homework
created by hiba srouji
'''
num = float(input('please enter your number '))

def pos_or_neg(num):
  if num > 0 :
    print(str(num) + ' is positive')
  elif num < 0:
    print(str(num) + ' is negative')
  else:
    print(str(num) + ' is zero')

pos_or_neg(num)

## the second function

x = int(input('please enter a positive number '))
def odd_or_even(x):
  if x == 0 :
    print(str(x) + ' the number is zero')
  elif (x % 2) == 0:
    print(str(x) + ' the number is even')
  else:
    print(str(x) + ' the number is odd')

odd_or_even(x)


## the third function
def SUM(num):
  x = 0
  for i in num:
    x = (x + i)
    print(x)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
SUM(list)

## the fourth function
def find_prime_50():
  for num in range(2, 51):
    for i in range(2, num):
      if(num % i == 0):
        break
      else:
        print(num)

find_prime_50()