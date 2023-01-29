"""2.	Выполнить функцию, которая принимает несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email,
телефон. Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой."""


def print_user(username, surname, birth, city, email, phone):
    print(
        f"Пользователь {username} {surname} {birth}-го года рождения, "
        f"проживающий в {city}, использует  Email {email} и телефон {phone}")


user_form = {
    'username': 'Имя',
    'surname': 'Фамилия',
    'birth': 'Год рождения',
    'city': 'Город проживания',
    'email': 'Email',
    'phone': 'Телефон'
}
new_user = {}
for key, value in user_form.items():
    input_value = input(f'{value}: ')
    new_user.update({key: input_value})

print_user(**new_user)
