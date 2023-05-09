import re
text = """ Hello I  am Shorya Tyagi ,pursuing b.tech from Computer Science
"""
# findall, search, split, su, finditer
patt = re.compile(r'Sho')
matches = patt.finditer(text)
for match in matches:
    print(match)

patt2 = re.compile(r'.yagi') #. represents character
matches2 = patt2.finditer(text)
for match1 in matches2:
    print(match1)

#! meta_characters
'''
     ^  starts with this in line or not  - re.compile(r'^sh)
     $  ends with - re.compile(r'b.tech$')
     *  Zero or more occurences - re.compile(r'ai*')
     + one or more occurences - re.compile(r'ai+')
     {} exactly the specific number of occurences - re.compile(r'ai{2})
     () capture and group - re.compile(r'(ai){2}')
     |  either or - re.compile(r'(ai){1}|t')
'''

#! Special Sequences

patt3 = re.compile(r'\AHello')
matches3 = patt3.finditer(text)

for match3 in matches3:
    print(match3)

'''
     \b - returns a match if the specified character is at the beginning of the word -rec.compile(r'\bhe')
     \d -  re.compile(r'\d{5}-\d{4})

'''
