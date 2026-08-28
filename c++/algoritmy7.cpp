#include <iostream>
#include <clocale>
#include <vector>
#include <algorithm>

using namespace std;

// Функция для вычисления характеристики строки (сумма отрицательных чётных)
int rowCharacteristic(const vector<int>& row) {
    int sum = 0;
    for (int val : row) {
        if (val < 0 && val % 2 == 0) {
            sum += val;
        }
    }
    return sum;
}

int main() {
    setlocale(LC_ALL, "ru_RU.UTF-8");
    
    int rows, cols;
    cout << "Введите количество строк и столбцов матрицы: ";
    cin >> rows >> cols;
    
    vector<vector<int>> mat(rows, vector<int>(cols));
    cout << "Введите элементы матрицы:\n";
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> mat[i][j];
        }
    }
    
    // 1. Поиск первого столбца, содержащего хотя бы один нулевой элемент
    int firstZeroCol = -1;
    for (int j = 0; j < cols; j++) {
        bool hasZero = false;
        for (int i = 0; i < rows; i++) {
            if (mat[i][j] == 0) {
                hasZero = true;
                break;
            }
        }
        if (hasZero) {
            firstZeroCol = j;   // индекс в коде (с 0)
            break;
        }
    }
    
    if (firstZeroCol != -1) {
        cout << "Номер первого столбца с нулевым элементом (нумерация с 1): " 
             << firstZeroCol + 1 << endl;
    } else {
        cout << "В матрице нет столбцов, содержащих нулевые элементы." << endl;
    }
    
    // 2. Вычисление характеристик строк
    vector<int> chars(rows);
    for (int i = 0; i < rows; i++) {
        chars[i] = rowCharacteristic(mat[i]);
    }
    
    // 3. Перестановка строк по убыванию характеристик (сортировка пузырьком или простая)
    //    Попутно переставляем и сами строки, и характеристики
    for (int i = 0; i < rows - 1; i++) {
        for (int j = i + 1; j < rows; j++) {
            if (chars[i] < chars[j]) {
                // обмен характеристик
                swap(chars[i], chars[j]);
                // обмен строк
                swap(mat[i], mat[j]);
            }
        }
    }
    
    // Вывод результатов
    cout << "\nМатрица после перестановки строк по убыванию характеристик:\n";
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << mat[i][j] << "\t";
        }
        cout << "   (характеристика = " << chars[i] << ")" << endl;
    }
    
    return 0;
}