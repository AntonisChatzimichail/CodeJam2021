def Reverse(lst):
    return [ele for ele in reversed(lst)]

T = input()
T = int(T)

for t in range(T):
    cost = 0
    N = input()
    N = int(N)
    line = input()
    array = line.split()

    for i in range(len(array)):
        array[i] = int(array[i])

    maxIdx = len(array) - 1
    for i in range(len(array) - 1):
        j = array.index(min(array[i:maxIdx+1]))
        array[i:j+1] = Reverse(array[i:j+1])
        cost += j - i + 1

    print("Case #" + str(t + 1) + ": " + str(cost))

