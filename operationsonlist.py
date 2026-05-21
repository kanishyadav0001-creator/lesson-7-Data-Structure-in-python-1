lst = ['Apple','Guava','Mango','Banana','Kiwi']

print("lenght of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Papaya')
print("Updated List :", lst)

lst.remove('Guava')
print("Upadated List:", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Upadated List:", lst)

lst.reverse()
print("Reversed List:", lst)

print("Multiplication on list :", lst*2)

lst = lst[:4]
print("Upadated List:", lst)

lst.clear()
print("Upadated List:", lst)

