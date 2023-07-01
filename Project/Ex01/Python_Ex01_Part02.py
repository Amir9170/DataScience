import collections , tabulate

s = collections.Counter(input('Please Enter your Sentence : '))
del s[' ']
print (tabulate.tabulate(s.items(), headers=["Name","Frequency"], tablefmt="grid"))