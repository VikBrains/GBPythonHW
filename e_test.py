var_1, var_2 = 20, 30
print(var_1, var_2)
var_1, var_2 = var_2, var_1
print(var_1, var_2)

my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}
# keys
print(my_dict.keys())

my_dict = {'k_1': 20, 'k_2': True, 'k_3': 'text'}
print(my_dict.get('k_4'))

my_list = [10, 10, 3, 4, 5, 9, 30, 30]
print(list(set(my_list)))
