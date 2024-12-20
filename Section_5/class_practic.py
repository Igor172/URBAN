class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    '''
    Класс пользователя создающий атрибуты: логин, пароль
    '''
    def __init__(self, username, password, password_cofirm):
        self.username = username
        if password == password_cofirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n')
        user = User(input('Введите логин: '), password := input('Введите пароль: '), password2 := input('Подтвердите пароль: '))
        if password != password2:
            exit()
    database.add_user(user.username, user.password)
    print(database.data)