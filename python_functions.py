#def greet():
  #  print("hello world")
 #   return 'Hi mars!'

#var=greet()
#print(var)


#def factorial(n):
    
    #fact = 1
   # for i in range (1 ,n+1):
  #      fact = fact * i
 #   return fact 
#fact_of_5 = factorial(5)
#fact_of_10 = factorial(10)

#print(fact_of_5)
#print(fact_of_10)

#def return_list():
 #   return[1,2,3,4]

#pdef bool():
  #  p = input('enter the string')
  #  for i in p:
    #    if i==p.upper():
   #         return[True]
  #      else:
 #           return[False]
#ans = bool()
#print(ans)

#from pickletools import string1


#def is_string_upper(string):
 #   return string.isupper()
#print(string)


#def sum_of_ascii(input_string):
 #   sum_= 0
  #  for i in input_string:
   #     sum_ += ord(i)
   # return 
#username = input('enter the name:')
#password = input('enter the password:')
#def generate(username,password):
  #  final = username[:4] + password[-4:]
 #   print(final)
#generate(username,password)

#char = input('enter character:')
#def character_index():
  #  total = 1
  #  for i in range(len(char)-1):
   #     if (ord(char[i])+1) == ord(char[i+1]):
  #          total +=1
 #       print(total)
#character_index(char)

list = [1,2,3,6]
def even_list(list):
    for i in list:
        if (int(i)%2 == 0):
            print('Even')
        else:
            print('odd')

even_list(list)
        






