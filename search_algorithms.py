#data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
target = 87450200

data = [*range(1, 100000000)]

def iterative_search(data, target):
    for i in range(len(data)):
        if i == target:
            print("found")
            print(target)
            return True
        else:
            i += 1
            #print(i)

#iterative_search(data, target)

print("====binary search on same data====")

def binary_search(data, target):
    low = 1
    high = len(data) - 1
    print("starting low: " + str(low) + " starting high: " + str(high))

    while low <= high:
        mid = (low + high) // 2
        print("\nstart loop")
        print("====================")
        print("mid: " + str(mid) + " low: " + str(low) + " high: " + str(high))
        if target == data[mid]:
            print("got it")
            result = mid+1
            print(result)
            return True
        elif target < data[mid]:
            print("target less than mid")
            high = mid - 1
            print("high = mid-1")
            print("high:")
            print(high)
            print("mid:")
            print(mid)
        else:
            print("target more than mid")
            low = mid + 1
            print("low = mid +1")
            print("low:")
            print(low)
            print("mid:")
            print(mid)
    #print(mid)
    return False
binary_search(data, target)

print("====recursive binary search on same data====")

def recursive_binary_search(data, target, low, high):
    if low > high:
        print("not found")
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            print("found")
            result = mid+1
            print(result)
            return True
        elif target < data[mid]:
            print(mid)
            return recursive_binary_search(data, target, low, mid-1)
        else:
            print(mid)
            return recursive_binary_search(data, target, mid+1, high)

#recursive_binary_search(data, target, 1, len(data)-1)