import re

def reverse(text):
    return text[::-1]#функция возвращает текст в зеркальном виде
def is_pallindrome(text):
    return text == reverse(text)

something = input('Введите текст:')
if is_pallindrome(''.join(re.findall(r'[a-z]+',something.lower()))):
    print('Да, это палиндром')
else:
    print('Нет, это не палиндром')
