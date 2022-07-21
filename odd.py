#no_of_inputs = input()
#no_of_inputs = int(no_of_inputs)

#lst=[]
#for i in range(no_of_inputs):
 #   some_input = input('Enter some input :')
  #  lst.append(some_input)
#print(lst)

no_of_elem = int(input())
map = {
   'str':[],
   'int':[],
   'float':[],

}

for i in range(no_of_elem):
   dt = input('enter datatype')
   value = input('enter value for above datatype:')
   if dt == 'str':
      map ['str'].append(value)
   elif dt == 'int':
      map ['int'].append(int(value))
   elif dt == 'float':
      map [float].append(float(value))
   else:
      print('please initialise a empty list ')