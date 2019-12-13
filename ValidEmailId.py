import re
str = input("enter the string:")
x=''

match=re.fullmatch(x,str)
if(match!=None):
    print("valid")
else:
    print("invalid")