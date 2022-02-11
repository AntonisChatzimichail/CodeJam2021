def swap(arr, e1, e2):
    tmp = arr[e1]
    arr[e1] = arr[e2]
    arr[e2] = tmp

def isGreaterThan(arr, e1, e2):
    res = False
    for i in range(len(arr)):
        if(arr[i] == e2):
            res = True
            break
        if(arr[i] == e1):
            break
    return res

def add(arr, low, high, x):
    # Check base case
    if high >= low:

        if low == high:
            return low

        mid = (high + low) // 2

        #search in right subarray
        print(str(arr[mid]) + " " + str(arr[high]) + " " + str(x))
        ans = input()
        ans = int(ans)
        if (ans == -1):
            print("Wrong answer or too many Qs, exiting...")
            exit(1)

        if(ans == arr[mid]):
            #x is on the left
            return add(arr, low, mid, x)
        elif(ans == arr[high]):
            #x is on the right
            return high + 1
        else:
            #x is in the middle
            return add(arr, mid + 1, high, x)

    else:
        # smth wrong
        return -1

line = input()
line = line.split()
T = int(line[0])
N = int(line[1])
Q = int(line[2])

for t in range(T):
    sArr = [1,2,3]
    print(str(1) + " " + str(2) + " " + str(3))
    ans = input()
    #print(ans)
    ans = int(ans)
    if(ans == -1):
        print("Wrong answer, exiting...")
        exit(1)
    swap(sArr, sArr.index(ans), sArr.index(2))
    #print(sArr)

    for i in range(4, N+1):
        addIdx = add(sArr, 0, len(sArr) - 1, i)
        if (addIdx == -1):
            print("Wrong addIdx, exiting...")
            exit(1)

        sArr.insert(addIdx, i)

    for i in range(N):
        print(str(sArr[i]), end = " ")
    print("")
    ans = input()
    ans = int(ans)
    if(ans == -1):
        print("Wrong answer, exiting...")
        exit(1)

