n = input('how many test cases: ')
n = int(n)
for i in range(n):
    op = input('enter the no')
    op_list = op.split()
    total = 0
    if op_list[0] == 'add':
       for j in op_list[1:]:
           total = total + int(j)
       print(total)