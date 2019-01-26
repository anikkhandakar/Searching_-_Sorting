

def linear_search(a, b):
    for i in a:
        if i == b:
            return True
    return False


List = [1, 6, 9, 7, 4, 50, 45, 98, 100, 26]
key = 98

if linear_search(List, key):
    print("Found")
else:
    print("Not Found!")
