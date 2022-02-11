T = input()
T = int(T)

for t in range(T):
    line = input()
    line = line.split()
    N = int(line[0])
    K = int(line[1])
    line = input()
    soldList = line.split()
    for i in range(len(soldList)):
        soldList[i] = int(soldList[i])
    soldSet = set(soldList)
    soldList = list(soldSet)
    soldList.sort()

    result = 0
    myFirst = -1
    myLast = -1
    for iter in range(2):
        idx = 0
        max_diff = 0
        start = 0
        end = 0
        for i in range(len(soldList) + 1):
            if i == 0:
                diff = soldList[0] - 1
                if diff > max_diff:
                    max_diff = diff
                    idx = -1
                    start = 1
                    end = soldList[0]
            elif i == len(soldList):
                diff = K - soldList[-1]
                if diff > max_diff:
                    max_diff = diff
                    idx = len(soldList) - 1
                    start = soldList[-1] + 1
                    end = K+1
            else:
                if soldList[i - 1] == myFirst:
                    continue
                if soldList[i - 1] != myLast:
                    diff = ((soldList[i] - soldList[i-1]) // 2)
                    if diff > max_diff:
                        max_diff = diff
                        idx = i - 1
                        start = soldList[i-1] + 1
                        end = start + diff
                else:
                    diff = (soldList[i] - soldList[i - 1]) - 1
                    if diff > max_diff:
                        max_diff = diff
                        idx = i - 1
                        end = soldList[i]
                        start = soldList[i-1] + 1


        pos = idx+1
        if end - start > 0:
            result += end - start
            myFirst = start
            myLast = end-1
            soldList.insert(pos, myFirst)
            soldList.insert(pos+1, myLast)

    #print(soldList)
    print("Case #" + str(t + 1) + ": " + str(result/K))
