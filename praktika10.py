def read_matrix_from_file(filename):
    """
    Чтение данных из файла для задания 1
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            
            n = int(lines[0].strip())
            
            
            matrix = []
            for i in range(1, n + 1):
                row = list(map(int, lines[i].strip().split()))
                matrix.append(row)
            
            
            m = int(lines[n + 1].strip())
            
            return n, matrix, m
            
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        return None, None, None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None, None, None

def write_results_to_file(filename, content):
    """
    Запись результатов в файл
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Результаты успешно записаны в файл {filename}")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

def task1(n, matrix, m):
    """
    Задание 1: Задана квадратная матрица. Переставить строку с максимальным элементом на главной диагонали со строкой с заданным номером m.
    """
    # создание копии матрицы
    result_matrix = [row[:] for row in matrix]
    
    
    max_index = 0
    for i in range(1, n):
        if result_matrix[i][i] > result_matrix[max_index][max_index]:
            max_index = i

    # переставляем строки
    if max_index != m - 1:
        result_matrix[max_index], result_matrix[m - 1] = result_matrix[m - 1], result_matrix[max_index]

    # результат
    result = "ЗАДАНИЕ 1:\n"
    result += f"Размер матрицы: {n}\n"
    result += f"Номер строки для замены (m): {m}\n"
    result += f"Строка с максимальным элементом на главной диагонали: {max_index + 1}\n\n"
    
    result += "Исходная матрица:\n"
    for row in matrix:
        result += ' '.join(map(str, row)) + '\n'
    
    result += "\nРезультирующая матрица:\n"
    for row in result_matrix:
        result += ' '.join(map(str, row)) + '\n'
    
    return result

def task2(n):
    """
    Задание 2: Составить программу, которая заполняет квадратную матрицу порядка п натуральными числами 1, 2, 3, … n2, записывая их в нее «по спирали».
    """
    matrix = [[0] * n for _ in range(n)]

    num = 1
    verh, dno = 0, n - 1
    left, right = 0, n - 1

    while num <= n * n:
        for i in range(left, right + 1):
            matrix[verh][i] = num
            num += 1
        verh += 1
        
        for i in range(verh, dno + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        for i in range(right, left - 1, -1):
            matrix[dno][i] = num
            num += 1
        dno -= 1
        
        for i in range(dno, verh - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    # Формируем результат
    result = "\nЗАДАНИЕ 2:\n"
    result += f"Матрица порядка {n}, заполненная по спирали:\n"
    for row in matrix:
        result += ' '.join(str(x) for x in row) + '\n'
    
    return result

def create_input_file():
    """
    Создание файла с входными данными для задания 1
    """
    input_content = """3
5 2 3
4 9 6
7 8 1
1"""
    
    last_name = "Чеченев"
    first_name = "Данил"
    middle_name = "Александрович"
    group = "УБ-52"
    
    input_filename = f"{last_name}_{first_name}_{middle_name}_{group}_vvod.txt"
    
    with open(input_filename, 'w', encoding='utf-8') as file:
        file.write(input_content)
    
    print(f"Файл с входными данными создан: {input_filename}")
    return input_filename

def main():
    """
    Основная функция программы
    """
    last_name = "Чеченев"
    first_name = "Данил"
    middle_name = "Александрович"
    group = "УБ-52"
    
    # имена файлов
    input_filename = f"{last_name}_{first_name}_{middle_name}_{group}_vvod.txt"
    output_filename = f"{last_name}_{first_name}_{middle_name}_{group}_vivod.txt"
    
    # создание файла с входными данными
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            pass
    except FileNotFoundError:
        print("Создаю файл с входными данными...")
        input_filename = create_input_file()
    
    print(f"Чтение данных из файла: {input_filename}")
    
    # Чтение данных для задания 1
    n, matrix, m = read_matrix_from_file(input_filename)
    
    results_content = "ПРАКТИЧЕСКАЯ РАБОТА №8\n"
    results_content += "ВАРИАНТ 14\n"
    results_content += "=" * 50 + "\n"
    
    # задание 1
    if n is not None and matrix is not None and m is not None:
        task1_result = task1(n, matrix, m)
        results_content += task1_result
    else:
        results_content += "Ошибка при выполнении задания 1: некорректные входные данные\n"
    
    results_content += "=" * 50 + "\n"
    
    # задание 2
    n_spiral = 5
    task2_result = task2(n_spiral)
    results_content += task2_result
    
    # вывод в файл
    write_results_to_file(output_filename, results_content)
    
    # вывод на экран
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ:")
    print("=" * 60)
    print(results_content)

if __name__ == "__main__":
    main()