text = input('Введите текст ') 

words = text.split()

words_start_with_a = []
words_end_with_ya = []

for word in words:
    lower_word = word.lower()
    
    if lower_word.startswith('а'):
        words_start_with_a.append(word)
    
    if lower_word.endswith('я'):
        words_end_with_ya.append(word)

print("Слова, которые начинаются на букву 'а':")
for word in words_start_with_a:
    print("-", word)

print("\nСлова, которые заканчиваются на букву 'я':")
for word in words_end_with_ya:
    print("-", word)