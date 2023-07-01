x1 = int(input('Please Enter a Number : '))
password = input('Please Enter the Password : ')
if password == 'abcd1234' and not x1 > 18:
    print ('OK, You Passed')
elif password == 'abcd1234' and x1 > 14:
    print ('OK, You Passed Naeloni')
else:
    print ('No, you have not Passed')