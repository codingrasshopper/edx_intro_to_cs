# Program to count number of occurences of "Bob"
import pdb
s = 'azcbobobobobegghaklbob'
count = 0
bobl = 3
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        count += 1
    
print count

    