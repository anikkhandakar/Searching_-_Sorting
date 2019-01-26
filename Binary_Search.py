

def binary_search(a, k):
    start = 0
    end = len(a)
    while start < end:
        mid = (start + end) // 2
        if a[mid] == k:
            return True
        elif k > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False


List = [1, 2, 3, 5, 6, 7, 8, 9, 10, 20, 65, 98, 458]
key = 11
if binary_search(List, key):
    print("Found")
else:
    print("Not Found!")
