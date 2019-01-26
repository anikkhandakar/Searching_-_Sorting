import random


def selection_sort(l):

    for i in range(len(l)-1):
        min_pos = i
        for j in range(i, len(l)):
            if l[j] < l[min_pos]:
                min_pos = j

        temp = l[i]
        l[i] = l[min_pos]
        l[min_pos] = temp


print()
List = []
for a in range(10):
    List.append(random.randrange(1, 101))
print(List)

print()
selection_sort(List)
print(List)