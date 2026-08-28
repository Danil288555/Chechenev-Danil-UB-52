#include <iostream>
#include <clocale>
#include <cmath>

using namespace std;

int main() {
    setlocale(LC_ALL, "ru_RU.UTF-8");
    
    const int n = 10;          // размер массива (можно изменить)
    double arr[n];
    
    cout << "Введите " << n << " вещественных элементов массива:\n";
    for (int i = 0; i < n; i++) {
        cout << "arr[" << i << "] = ";
        cin >> arr[i];
    }
    
    // 1. Минимальный элемент
    double min_val = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < min_val) {
            min_val = arr[i];
        }
    }
    cout << "\n1) Минимальный элемент массива: " << min_val << endl;
    
    // 2. Сумма элементов между первым и последним положительными элементами
    int first_pos = -1, last_pos = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] > 0) {
            if (first_pos == -1) first_pos = i;
            last_pos = i;
        }
    }
    
    double sum_between = 0.0;
    if (first_pos != -1 && last_pos != -1 && first_pos < last_pos - 1) {
        for (int i = first_pos + 1; i < last_pos; i++) {
            sum_between += arr[i];
        }
    }
    cout << "2) Сумма элементов между первым и последним положительными: "
         << sum_between << endl;
    
    // 3. Преобразование: сначала все отрицательные, затем остальные
    // Используем метод двух указателей (сортировка отрицательных в начало)
    int writePos = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] < 0) {
            swap(arr[i], arr[writePos]);
            writePos++;
        }
    }
    
    cout << "3) Преобразованный массив (отрицательные → в начало):" << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}