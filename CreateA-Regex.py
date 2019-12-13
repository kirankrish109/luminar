import re
str = input("enter the string:")
x='91[6-9]\d{9}'

match=re.fullmatch(x,str)
if(match!=None):
    print("valid")
else:
    print("invalid")