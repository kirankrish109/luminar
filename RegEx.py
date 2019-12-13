import re
# x='[abc]'

# x='[A-Z]'
# x='[abc]'
# x='[0-9]'
# x='[a-zA-Z0-9]'
# x='[^a-zA-Z0-9]'
#
# x='\s'#space
# x='\D'#not digit
# x='\d'#digits

# x='a*'
# #
# x='a+'
x='a?'
# count = 0
# matcher=re.finditer('ab','abaababa')
# for match in matcher:
#     print(match)
#     print("match available at ",match.start())
#     print("group=",match.group())
#     count +=1
# print("count=",count)



matcher=re.finditer(x,'abaabbaaabbb')
for match in matcher:
    print("match available at ",match.start())
    print("group=",match.group())