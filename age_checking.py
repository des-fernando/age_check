# Age checking

age = int(input('Type your age: '))

if age < 18:
    print('You\'re a kid!')
elif age > 18 and age < 60:
    print('You\'re and adult!')
else:
    print('You\'re elder!')