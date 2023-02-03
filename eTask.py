"""2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""

"""task_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []

for i in task_list:
    i = 1
    j = i - 1
    if i > j:
        new_list.append(i)
    i += 1
    continue

print(f"целевой лист: {new_list}")"""

# for ex
# new_list = [i for i in my_list if i < j]
# i = 1

task_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_result = [k for i, j in enumerate(task_list) for k in task_list
[(i + 1):(i + 2)] if k > j]
print(list_result)