import re

s = "My 2 favorite numbers are 42 and 19"
re.findall("[0-9]",s)
['2', '4', '2', '1', '9']


s1 = "An apple a day keeps the doctor away"
re.findall("[AEIOUaeiou]", s1)
['A', 'a', 'e', 'a', 'a', 'ee', 'e', 'o', 'o', 'a', 'a']


s = "My 2 favorite numbers are 42 and 19"
re.findall("[0-9]+",s)
#Will accept more than 1 occurence of adjacent numebr as well (42, 19)
['2', '42', '19']


s = "My 2 favorite numbers are 42 and 19"
re.findall("[^0-9]+",s)
#Everything except numbers
['My ', ' favorite numbers are ', ' and ']

s1 = "An apple a day keeps the doctor away"
re.findall("[aeiou]+", s1)
#Will accept words having one or more occurence of vowel
['A', 'a', 'e', 'a', 'a', 'e', 'e', 'e', 'o', 'o', 'a', 'a']


s1 = "An apple a day keeps the doctor away"
re.findall("[AEIOUaeiou]+", s1)
['A', 'a', 'e', 'a', 'a', 'ee', 'e', 'o', 'o', 'a', 'a']


re.findall("\s",s)
[' ', ' ', ' ', ' ', ' ', ' ', ' ']


re.findall("\S",s)
['M',
 'y',
 '2',
 'f',
 'a',
 'v',
 'o',
 'r',
 'i',
 't',
 'e',
 'n',
 'u',
 'm',
 'b',
 'e',
 'r',
 's',
 'a',
 'r',
 'e',
 '4',
 '2',
 'a',
 'n',
 'd',
 '1',
 '9']


s2 = "sat pat hat mat"
re.findall("at", s2)
['at', 'at', 'at', 'at']


s2 = "sat pat hat mat"
re.findall(".at$", s2)
#Dollar will give end of the line having at at the end
['mat']


s2 = "sat pat hat mat"
re.findall("[h-m]at", s2)
#Will give word starting with from h to m and ending with at
['hat', 'mat']


s2 = "sat pat hat mat"
re.findall("[A-Z][a-z]at", s2)
#Will give word starting with upper case and lowercase ending with at
[]


s2 = "MY email id is abc@gmail.com and i received a mail on this"
re.findall("[a-z]+@[a-z]+.\S{3}", s2)
['abc@gmail.com']


s3 = 'G-34GRADING system offers: 3432 weightage to: 32 units'
re.findall(".*:", s3)
#Everything 0 or more number of times before :


re.findall(".+?:", s3)
#Non linear which starts a new list element after :
['G-34GRADING system offers:', ' 3432 weightage to:']
