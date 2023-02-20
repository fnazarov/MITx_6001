'''
a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl',  program  print:

Number of vowels: 5

'''

vowels='aeiou'
count=0
for i in s:
    if i in vowels:
        count+=1
print("Number of vowels: ",count)

'''
Assume s is a string of lower case characters.

Code that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then  program  print

Number of times bob occurs is: 2
'''
st='bob'
count=0
#s = 'joboobobnebfbbobob'
for i in range(len(s)):
    if s[i:i+3]==st:
        count+=1
print("Number of times bob occurs is: ",count)

'''
Assume s is a string of lower case characters.

Code that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then code print

Longest substring in alphabetical order is: beggh
'''
cs=s[0]
ls=s[0]

for i in range(1,len(s)):
    if s[i]>=cs[-1]:
        cs+=s[i]
        if len(cs)>len(ls):
            ls=cs
    else:
        cs=s[i]
print("Longest substring in alphabetical order is: ",ls)