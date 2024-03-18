my_list = list(range(1, 101))
new2_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new2_list)
print(my_list)
