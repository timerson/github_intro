#!/usr/bin/env python3
number = input('Enter a number and I will tell you how many binary bits are the logic level 1:')
x = int(number)
count = 0
iterations = 0
while x != 0:
    count += x & 1
    iterations += 1
    x = x >> 1
print ('It took me ' + str(iterations) + ' times to determine ' + number + ' has ' + str(count) + ' bits on')
if count == 1:
    print ('and ' + number + ' is a power of two!')
    


       
