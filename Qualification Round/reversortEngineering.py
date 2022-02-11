def Reverse(lst):
    return [ele for ele in reversed(lst)]

def sumInt(start, end):
    res = 0
    for i in range(start, end):
        res += i
    return res

T = input()
T = int(T)

for t in range(T):
    array = list()
    costArray = list()
    line = input()
    line = line.split()
    N = int(line[0])
    C = int(line[1])

    if(C < N-1 or C > sumInt(2, N+1)):
        print("Case #" + str(t + 1) + ": IMPOSSIBLE")
        continue

    for i in range(N):
        array.append(i+1)

    for i in range(N-1):
        costArray.append(1)

    rem = C - (N - 1)

    for i in range(N-1):
        if(rem == 0):
            break
        maxCost = N - i
        if (costArray[i] + rem > maxCost):
            costArray[i] = maxCost
            rem -= maxCost - 1
        else:
            costArray[i] += rem
            rem = 0

    for i in range(N - 2, -1, -1):
        j = costArray[i] + i - 1
        array[i:j + 1] = Reverse(array[i:j + 1])

    print("Case #" + str(t + 1) + ":", end=" ")
    for elem in array:
        print(elem, end = " ")
    print("")
    #print(costArray)
