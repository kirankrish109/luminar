lines="ABCCABA"


dict={}
for word in lines:
    if(word  in dict):

        print(word,"is the first recursive word")
        break
    else:
        dict[word] = 1





