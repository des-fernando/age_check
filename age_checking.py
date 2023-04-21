age = int(input('Type your age: '))

def age_checking():
    if age <= 12:
        print(f'You are {age} years old, then you\'re a kid!')
    elif age >= 12 and age < 18:
        print(f'You are {age} years old, then you\'re a teen!')
    elif age >= 18 and age <= 59:
        print(f'You are {age} years old, then you\'re an adult!')
    elif age >= 60 and age < 110:
        print(f'You are {age} years old, then you\'re elder!')
    else:
        print(f'Wow, you are {age} years old, you\'re a Dinosaur!')
    
age_checking()
