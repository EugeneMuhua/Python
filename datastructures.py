my_list = []
print("1.", my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("2.", my_list)

my_list.insert(1, 15)
print("3.", my_list)

my_list.extend([50, 60, 70])
print("4.", my_list)

remove= my_list.pop()
print("5.", my_list, "removed:", remove)

my_list.sort()
print("6.", my_list)

index_30= my_list.index(30)
print("7. Index of 30 is equated to", index_30)