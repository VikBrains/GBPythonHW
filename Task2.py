"""Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк."""
time_co = int(input("Сколько секунд до следующего занятия? "))
time_hour = (time_co // 3600)
time_h_rem = (time_co % 3600)
time_min = (time_h_rem // 60)
time_sec = (time_h_rem % 60)
print(f"{time_hour}:{time_min}:{time_sec}")