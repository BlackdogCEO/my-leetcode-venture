print("please input a list of numbers")
L = list(input().split())
print(L)
print(L.__len__())
l = [int(i) for i in L]
print(l)
print("please input the value you want to search")
value = input()
value = int(value)
if not l:
    print("no value in list")
low = 0
high = len(l) - 1
while low <=high:
    mid = int((low + high) / 2)
    if value == l[mid]:
        print("{} is the {}th number in the list" .format(value, mid+1))
        exit()
    elif value > l[mid] and:
        if l[mid] > l[high]:
            low = mid + 1
        else:
            if value > l[high]:
                high = mid - 1
            else:
                low = mid + 1
    elif value < l[mid]:
        if l[mid] < l[high]:
            high = mid - 1
        else:
            if value < l[low]:
                low = mid + 1
            else:
                high = mid - 1

print("not found")
