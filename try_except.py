try:
    text = input('Введите что - нибудь')
except EOFError:
    print('Ну зачем вы сделалии мне E0F???') # ввести ctrl - d
except KeyboardInterrupt:
    print('Вы отменили операцию') # ввести ctrl - f2
else: # отрабатывает когда исключений не возникает
    print('Вы ввели: {}'.format(text))