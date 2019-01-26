import random


def bubble_sort(l):

    ite = len(l) - 1
    while ite > 0:

        for i in range(0, ite):
            if l[i] > l[i + 1]:
                temp = l[i]
                l[i] = l[i + 1]
                l[i + 1] = temp

        ite = ite - 1


# List = [9, 65, 9, 8, 7, 54, 56, 2, 12, 3, 236, 2, 5456, 5, 578, 365]
# List = [9, 65, 9, 8, 7, 54, 56]

print()
List = []
for a in range(10):
    List.append(random.randrange(1, 50))
print(List)

print()
bubble_sort(List)
print(List)


