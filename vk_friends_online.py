import getpass
import vk


APP_ID = 5128435


def get_user_login():
    login = input('Введите логин пользователя: ')
    return login


def get_user_password():
    password = getpass.getpass('Введите пароль пользователя: ')
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    id_friends_online = api.friends.getOnline()
    if id_friends_online:
        return api.users.get(user_ids=id_friends_online)
    else:
        return []


def output_friends_to_console(friends_online):
    if not friends_online:
        print('Нет друзей в сети.')
        return
    for friend in friends_online:
        friend_name = '%s %s' % (friend['first_name'],
                                 friend['last_name'])
        print(friend_name)


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
