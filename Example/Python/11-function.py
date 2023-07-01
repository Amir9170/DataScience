def say_hello(first_name , last_name):
    print ('Hello', first_name)
    print ('Goodbye', last_name)

i = 10
j = 20
say_hello('Amir' , 'Rasoulzadeh')

print ('Last Line')

def get_age(name , family = 'Rasoulzadeh'):
    if name == 'Amir':
        return 31
    elif name == 'Omid':
        return 29
    else:
        return -1
    
age = get_age(input('Enter Your Name : '))
print (age)