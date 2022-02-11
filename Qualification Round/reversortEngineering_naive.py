def Reverse(lst):
    return [ele for ele in reversed(lst)]

def inversionStep(myArray, cost, i):
    #print(str(i) + ": Current array " + str(myArray) + " with cost " + str(cost))

    if (cost > C):
        #print("Too much cost")
        return list()

    if (i == -1):
        if( cost == C):
            #print("Found solution")
            return list(myArray)
        #print("Not a solution")
        return list()

    maxIdx = len(array) - 1
    for j in range(maxIdx, i-1, -1):
        nextArray = list(myArray)
        nextArray.insert(0, j)
        newCost = cost + j - i + 1
        #print(str(i) + ": Current array " + str(myArray) + " is calling " + str(nextArray))
        resArray = inversionStep(nextArray, newCost, i-1)
        if(len(resArray) != 0):
            return list(resArray)

    return list()

T = input()
T = int(T)

for t in range(T):
    array = list()
    stepArray = list()
    line = input()
    line = line.split()
    N = int(line[0])
    C = int(line[1])

    for i in range(N):
        array.append(i+1)

    stepArray = inversionStep(stepArray, 0, len(array) - 2)

    print("Case #" + str(t + 1) + ":", end = " ")
    if(len(stepArray) == 0):
        print("IMPOSSIBLE")
    else:
        for i in range(len(array) - 2, -1, -1):
            j = stepArray[i]
            array[i:j + 1] = Reverse(array[i:j + 1])
        for elem in array:
            print(elem, end = " ")
        print("")
