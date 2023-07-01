s = input('Please Enter your Sentence : ')
count = {}
for i in s:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1
del count[' ']

print ('+--------+-------------+')
print ("| Name  " , '|',"  Frequency |")
print ('+--------+-------------+')
for i in count:
    print ('|',i,'     |          ',count[i],'|')
    print ('+--------+-------------+')