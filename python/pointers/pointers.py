# When two vaiables are pointed at each other and one is updated the other doesnt update
num1 = 11

num2 = num1

print('Before the num values are updated: ')
print('Num1 = ', num1)
print('Num2 = ', num2)

print("\nnum1 points to: ",id(num1))
print("num2 points to: ",id(num2))

num2 = 22

print('\nAfter the num2 values are updated: ')
print('Num1 = ', num1)
print('Num2 = ', num2)

print("\nnum1 points to: ",id(num1))
print("num2 points to: ",id(num2))

# When a dictionary is othe and one of the them have the value changed the other updates as well
dict1 = {'value': 11}

dict2 = dict1

print('\n\nBefore the dict values are updated: ')
print('dict1 = ', dict1)
print('dict2 = ', dict2)

print("\ndict1 points to: ",id(dict1))
print("dict2 points to: ",id(dict2))

dict2['value'] = 22

print('\nAfter the dict2 values are updated: ')
print('dict1 = ', dict1)
print('dict2 = ', dict2)

print("\ndict1 points to: ",id(dict1))
print("dict2 points to: ",id(dict2))
