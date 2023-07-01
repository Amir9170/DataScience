import random
import string
c = input('Please Enter Number of Character : ')
t = string.ascii_letters + string.digits
print (''.join(random.sample(t+t+t , int(c))))