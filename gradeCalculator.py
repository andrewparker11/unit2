#Andrew Parker
#9/13/17
#gradeCalculator.py - Converts numerical grades to letter grades

grade = float(input('Enter a number: '))
if 101>grade>92:
    print('You earned an A')
elif grade>92:
    print('You earned an A-')
elif grade>86:
    print('You earned an B+')
elif grade>82:
    print('You earned an B')
elif grade>79:
    print('You earned an B-')
elif grade>76:
    print('You earned an C+')
elif grade>72:
    print('You earned an C')
elif grade>69:
    print('You earned an C-')
elif grade>0:
    print('Get out.')
    
