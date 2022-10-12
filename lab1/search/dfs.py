import util 

test=util.Stack()
test.push('1')
test.push('2')

flag=0
if '2' in test:
    print("yeay!")
while not(test.isEmpty()):
    print(test.pop())
