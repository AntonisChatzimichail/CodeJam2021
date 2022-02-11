def Evaluate(stringList):
    cost = 0
    for i in range(1, len(stringList)):
        if(stringList[i-1] == 'C' and stringList[i] == 'J'):
            cost += X
        elif(stringList[i-1] == 'J' and stringList[i] == 'C'):
            cost += Y
    return cost

T = input()
T = int(T)

for t in range(T):
    line = input()
    line = line.split()
    X = int(line[0])
    Y = int(line[1])
    string = line[2]
    sList = list(string)

    firstLetter = 0
    while(1):
        if(firstLetter >= len(sList)):
            sList[0] = 'C'
            firstLetter = 0
            break
        if(sList[firstLetter] != '?'):
            break
        firstLetter += 1

    for i in range(firstLetter + 1):
        sList[i] = sList[firstLetter]

    for i in range(firstLetter + 1, len(sList)):
        if(sList[i] != '?'):
            continue
        tempListC = list('C')
        tempListJ = list('J')
        if(i > 0):
            tempListC.insert(0, sList[i - 1])
            tempListJ.insert(0, sList[i - 1])
        if(i < firstLetter):
            tempListC.append(sList[i + 1])
            tempListJ.append(sList[i + 1])
        resC = Evaluate(tempListC)
        resJ = Evaluate(tempListJ)

        if(resC < resJ):
            sList[i] = 'C'
        else:
            sList[i] = 'J'

    #print(sList)
    print("Case #" + str(t + 1) + ": " + str(Evaluate(sList)))
