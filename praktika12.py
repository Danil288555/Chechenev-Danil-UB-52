import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import requests
from datetime import datetime

class GitHubRepoInfo:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Repository Info - Вариант 9")
        self.root.geometry("750x600")
        self.root.resizable(True, True)
        self.setup_ui()
    
    def setup_ui(self):
        # Основной фрейм
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # растягивание
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Заголовок
        title_label = ttk.Label(main_frame, 
                               text="GitHub Repository Information", 
                               font=("Arial", 16, "bold"),
                               foreground="darkblue")
        title_label.grid(row=0, column=0, pady=(0, 10))
        
        # Инфо о репозитории
        repo_info_frame = ttk.LabelFrame(main_frame, text="Информация о репозитории", padding="10")
        repo_info_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        repo_info_frame.columnconfigure(1, weight=1)
        
        ttk.Label(repo_info_frame, text="Репозиторий:", font=("Arial", 10, "bold")).grid(
            row=0, column=0, sticky=tk.W, pady=2)
        ttk.Label(repo_info_frame, text="Automattic/wp-calypso", font=("Arial", 10)).grid(
            row=0, column=1, sticky=tk.W, pady=2)
        
        ttk.Label(repo_info_frame, text="Ссылка:", font=("Arial", 10, "bold")).grid(
            row=1, column=0, sticky=tk.W, pady=2)
        ttk.Label(repo_info_frame, text="https://github.com/Automattic/wp-calypso", 
                 foreground="blue", font=("Arial", 10)).grid(
            row=1, column=1, sticky=tk.W, pady=2)
        
        ttk.Label(repo_info_frame, text="Вариант:", font=("Arial", 10, "bold")).grid(
            row=2, column=0, sticky=tk.W, pady=2)
        ttk.Label(repo_info_frame, text="9", font=("Arial", 10)).grid(
            row=2, column=1, sticky=tk.W, pady=2)
        
        # Кнопка
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=15)
        
        self.get_info_btn = ttk.Button(button_frame, 
                                      text="Получить информацию о репозитории", 
                                      command=self.get_repo_info)
        self.get_info_btn.grid(row=0, column=0, padx=5)
        
        self.save_btn = ttk.Button(button_frame, 
                                  text="Сохранить в файл", 
                                  command=self.save_to_file,
                                  state="disabled")
        self.save_btn.grid(row=0, column=1, padx=5)
        
        # вывод JSON
        output_frame = ttk.LabelFrame(main_frame, text="Результат в формате JSON", padding="10")
        output_frame.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        self.json_text = scrolledtext.ScrolledText(output_frame, 
                                                  width=80, 
                                                  height=20, 
                                                  font=("Consolas", 10),
                                                  wrap=tk.WORD)
        self.json_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Статус бар
        self.status_var = tk.StringVar()
        self.status_var.set("Готов к работе")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # сохранение
        self.repo_data = None
    
    def get_repo_info(self):
        """Получение информации о репозитории Automattic/wp-calypso через GitHub API"""
        self.status_var.set("Получение данных...")
        self.root.update()
        
        repo_name = "Automattic/wp-calypso"
        
        try:
            # Делаем запрос к GitHub API
            response = requests.get(f"https://api.github.com/repos/{repo_name}")
            
            if response.status_code == 200:
                repo_data = response.json()
                
                # Получаем информацию о владельце
                owner_url = repo_data['owner']['url']
                owner_response = requests.get(owner_url)
                
                if owner_response.status_code == 200:
                    owner_data = owner_response.json()
                    
                    # Формируем данные
                    self.repo_data = {
                        'company': owner_data.get('company'),
                        'created_at': owner_data.get('created_at'),
                        'email': owner_data.get('email'),
                        'id': owner_data.get('id'),
                        'name': owner_data.get('login'),
                        'url': owner_data.get('url')
                    }
                    
                    # Показываем информацию
                    self.json_text.delete(1.0, tk.END)
                    formatted_json = json.dumps(self.repo_data, indent=4, ensure_ascii=False)
                    self.json_text.insert(tk.END, formatted_json)
                    
                    # Активируем кнопку сохранения
                    self.save_btn.config(state="normal")
                    
                    self.status_var.set(" Данные успешно получены")
                    messagebox.showinfo("Успех", "Информация о репозитории успешно получена!")
                    
                else:
                    self.status_var.set(" Ошибка получения данных владельца")
                    messagebox.showerror("Ошибка", 
                                       f"Ошибка получения данных владельца: {owner_response.status_code}")
                    
            elif response.status_code == 404:
                self.status_var.set(" Репозиторий не найден")
                messagebox.showerror("Ошибка", "Репозиторий не найден")
            else:
                self.status_var.set(" Ошибка API GitHub")
                messagebox.showerror("Ошибка", f"Ошибка API GitHub: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            self.status_var.set(" Ошибка подключения")
            messagebox.showerror("Ошибка", f"Ошибка подключения: {e}")
        except Exception as e:
            self.status_var.set(" Неожиданная ошибка")
            messagebox.showerror("Ошибка", f"Неожиданная ошибка: {e}")
    
    def save_to_file(self):
        """Сохранение данных в JSON файл"""
        if not self.repo_data:
            messagebox.showerror("Ошибка", "Нет данных для сохранения")
            return
        
        try:
            # имя файла с временной меткой
            filename = f"github_repo_info_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.repo_data, file, indent=4, ensure_ascii=False)
            
            self.status_var.set(f" Данные сохранены в файл: {filename}")
            messagebox.showinfo("Успех", 
                              f"Данные успешно сохранены в файл:\n{filename}\n\n"
                              f"Файл создан в текущей директории.")
            
        except Exception as e:
            self.status_var.set(" Ошибка сохранения")
            messagebox.showerror("Ошибка", f"Ошибка при сохранении файла: {e}")

def main():
    root = tk.Tk()
    
    # Настройка стиля для акцентной кнопки
    style = ttk.Style()
    style.configure("Accent.TButton", foreground="white", background="#0078d4")
    
    app = GitHubRepoInfo(root)
    root.mainloop()

if __name__ == "__main__":
    main()