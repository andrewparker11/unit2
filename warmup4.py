#Andrew Parker
#9/18/17
#warmup4.py - if has 7 or divisble by 7 says Buzz

num = int(input('Input a Number'))
if '7' in str(num) or num%7 == 0:
    print('Buzz')
else:
    print(num)