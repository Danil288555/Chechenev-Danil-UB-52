import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# окно
root = tk.Tk()
root.title("Чеченев Данил Александрович")
root.geometry("500x400")

# вкладки
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Текст')

tab_control.pack(expand=1, fill='both')

# калькулятор
tk.Label(tab1, text="Первое число:").pack(pady=5)
num1_entry = tk.Entry(tab1)
num1_entry.pack(pady=5)

tk.Label(tab1, text="Операция:").pack(pady=5)
operation_var = tk.StringVar(value="+")
operation_combo = ttk.Combobox(tab1, textvariable=operation_var, values=["+", "-", "*", "/"])
operation_combo.pack(pady=5)

tk.Label(tab1, text="Второе число:").pack(pady=5)
num2_entry = tk.Entry(tab1)
num2_entry.pack(pady=5)

result_label = tk.Label(tab1, text="Результат: ")
result_label.pack(pady=10)

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        
        result_label.config(text=f"Результат: {result}")
    except:
        messagebox.showerror("Ошибка", "Проверьте правильность ввода")

tk.Button(tab1, text="Вычислить", command=calculate).pack(pady=10)

# чекбоксы
checkbox1_var = tk.BooleanVar()
checkbox2_var = tk.BooleanVar()
checkbox3_var = tk.BooleanVar()

tk.Checkbutton(tab2, text="Первый", variable=checkbox1_var).pack(pady=10)
tk.Checkbutton(tab2, text="Второй", variable=checkbox2_var).pack(pady=10)
tk.Checkbutton(tab2, text="Третий", variable=checkbox3_var).pack(pady=10)

def show_selection():
    selected = []
    if checkbox1_var.get():
        selected.append("первый")
    if checkbox2_var.get():
        selected.append("второй")
    if checkbox3_var.get():
        selected.append("третий")
    
    if selected:
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selected)}")
    else:
        messagebox.showinfo("Выбор", "Вы ничего не выбрали")

tk.Button(tab2, text="Показать выбор", command=show_selection).pack(pady=20)

# работа с текстом
text_widget = tk.Text(tab3, height=15)
text_widget.pack(padx=10, pady=10, fill='both', expand=True)

def load_text():
    file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            text_widget.delete(1.0, tk.END)
            text_widget.insert(1.0, text)
        except:
            messagebox.showerror("Ошибка", "Не удалось загрузить файл")

tk.Button(tab3, text="Загрузить текст из файла", command=load_text).pack(pady=10)

# запуск
root.mainloop()