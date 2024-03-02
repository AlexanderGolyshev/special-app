my_list = list(range(1, 101))
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)
