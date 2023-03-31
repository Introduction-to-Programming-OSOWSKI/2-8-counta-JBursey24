def countA(word):
    numA=0
    for i in range(0,len(word)):
        if word[i]=="a":
            numA = numA+1
    return str(numA)