
text = list()

with open("text.txt") as file:
    for items in file:
        text += list(items)

    
def word2ngrams(b, n):
    ban = set("0123456789 .,!?:;«»%-+=/\n")
    ngrams = []
    flag = False
    for i in range(len(b) - n + 1):
        k = 0
        while k != n:
            if b[i+k] in ban:
                flag = True
            k+=1

        if (flag):
            flag = False
            continue
        else:
            ngrams.append("".join(b[i:i + n]))
    return ngrams


print(word2ngrams(text,2))
print(word2ngrams('foo; bar bar black \n sheep',2))

