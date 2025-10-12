text = input('Введите текст: ' )
word = input('Какое слово ищем? ')
count = text.lower().count(word.lower())
print(count)