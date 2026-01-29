# Импортируем необходимые элементы из библиотеки Flask
# Flask используется для создания веб-приложений
from flask import Flask, request, render_template_string


# Создаём объект веб-приложения
# __name__ указывает на текущий файл программы
app = Flask(__name__)


# HTML-шаблон страницы
# В нём описывается структура веб-страницы и форма ввода данных
html_page = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Генератор резюме</title>
</head>
<body>
    <h1>Генератор резюме</h1>


    <!-- Форма для ввода данных пользователя -->
    <!-- method="post" означает отправку данных на сервер -->
    <form method="post">
        <p>Имя и фамилия:<br><input type="text" name="name"></p>
        <p>Контакты:<br><input type="text" name="contacts"></p>
        <p>Образование:<br><textarea name="education"></textarea></p>
        <p>Навыки:<br><textarea name="skills"></textarea></p>
        <p>Опыт работы:<br><textarea name="experience"></textarea></p>
        <button type="submit">Сгенерировать резюме</button>
    </form>


    <!-- Если резюме сформировано, оно выводится ниже -->
    {% if resume %}
    <h2>Ваше резюме</h2>
    <pre>{{ resume }}</pre>
    {% endif %}
</body>
</html>
"""


# Декоратор route указывает, что функция index
# будет вызываться при переходе на главную страницу сайта
@app.route('/', methods=['GET', 'POST'])
def index():
    # Переменная resume хранит готовый текст резюме
    # По умолчанию резюме отсутствует
    resume = None


    # Проверяем, была ли отправлена форма
    if request.method == 'POST':
        # Получаем данные, введённые пользователем
        name = request.form.get('name', '')
        contacts = request.form.get('contacts', '')
        education = request.form.get('education', '')
        skills = request.form.get('skills', '')
        experience = request.form.get('experience', '')


        # Формируем текст резюме из введённых данных
        # Используются форматированные строки (f-strings)
        resume = (
        f"Имя: {name}\n"
        f"Контакты: {contacts}\n\n"
        f"Образование:\n{education}\n\n"
        f"Навыки:\n{skills}\n\n"
        f"Опыт работы:\n{experience}"
    )


    # Возвращаем HTML-страницу и передаём в неё текст резюме
    return render_template_string(html_page, resume=resume)


# Проверка, что файл запущен напрямую
if __name__ == '__main__':
    # Запуск локального веб-сервера
    # debug=True используется для удобства отладки
    app.run(debug=True)