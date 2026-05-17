import json
# Открываем файл data.json в режиме чтения с кодировкой utf-8
with open('data.json', 'r', encoding='utf-8') as f:
    # Загружаем содержимое файла в переменную data (это будет словарь)
    data = json.load(f)
# Извлекаем список событий по ключу 'events_data'
events = data['events_data']
# Создаём пустые множества для хранения уникальных client_id
all_clients = set()      # все клиенты из всех событий
date_clients = set()     # клиенты, у которых есть action с category = 'datepicker'
table_clients = set()    # клиенты, у которых есть action с category = 'table'
report_clients = set()   # клиенты, у которых есть action с category = 'report'
# Перебираем каждое событие в списке events
for event in events:
    # Получаем client_id из текущего события
    cid = event['client_id']
    # Получаем category из текущего события
    cat = event['category']
    
    # Добавляем client_id в множество всех клиентов
    all_clients.add(cid)
    
    # В зависимости от категории добавляем client_id в соответствующее множество
    if cat == 'datepicker':
        date_clients.add(cid)      # клиент использовал выбор даты
    elif cat == 'table':
        table_clients.add(cid)     # клиент сортировал таблицу
    elif cat == 'report':
        report_clients.add(cid)    # клиент работал с отчётами

# Задание 5
# Находим клиентов, которые НЕ совершали действий с datepicker И НЕ с table
# Для этого из всех клиентов вычитаем объединение множеств date_clients и table_clients
# Объединение (date_clients | table_clients) – клиенты, у которых есть хотя бы одно из этих действий
clients_without_dt = all_clients - (date_clients | table_clients)
# Количество таких клиентов – длина полученного множества
result_5 = len(clients_without_dt)
# Задание 15
# Проверяем, есть ли клиенты с category='report'
if report_clients:
    # Находим минимальный client_id среди множества report_clients
    result_15 = min(report_clients)
else:
    result_15 = None   # если таких клиентов нет, то результат None

# Выводим результаты на экран
print(f"5. Клиентов без datepicker и table: {result_5}")
print(f"15. Минимальный client_id (report): {result_15}")