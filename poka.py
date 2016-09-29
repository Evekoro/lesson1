while True:
        user_say = input('Скажи что-нибудь: ')
        if user_say.lower() == 'пока':
            print('Ну пока')
            break
        else:
            print('Сам ты %s' % user_say)