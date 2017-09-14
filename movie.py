#Andrew Parker
#9/13/17
#movie.py - Gives most scandalous movie rating you can watch by age

age = int(input('Enter your age: '))
if age>0:
    print('The most scandalous movie you can watch is G-rated')
elif 10>age>7:
    print('The most scandalous movie you can watch is PG rated')
elif 13>age>10:
    print('The most scandalous movie you can watch is PG-13 rated with a parent or guardian')
elif 17>age>13:
    print('The most scandalous movie you can watch is R rated with a parent or guardian')
elif 200>age>17:
    print('Watch whatever you want')
