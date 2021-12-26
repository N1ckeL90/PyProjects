from sys import exit


def user_hobby(users_file, hobby_file, users_hobby):
    with open(users_file, encoding='utf-8') as fr1:
        with open(hobby_file, encoding='utf-8') as fr2:
            with open(users_hobby, 'w', encoding='utf-8') as fw:
                for user in fr1:
                    hobby = fr2.readline()
                    if hobby == '':
                        hobby = 'None'
                    str_tmp = f'{user.rstrip()}: {hobby.rstrip()}\n'
                    fw.writelines(str_tmp)
                # Если данных о хобби больше количества ФИО
                user = fr1.readline()
                hobby = fr2.readline()
                if user == '' and hobby != '':
                    exit(1)


user_hobby('users.csv', 'hobby.csv', 'users_hobby.txt')
