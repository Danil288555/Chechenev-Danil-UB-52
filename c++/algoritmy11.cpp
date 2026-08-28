#include <iostream>
#include <fstream>
#include <clocale>

using namespace std;

int main() {
    setlocale(LC_ALL, "ru_RU.UTF-8");
    
    const int n = 10;
    int arr[n];
    
    // Чтение из файла
    ifstream fin("input.txt");
    if (!fin) {
        cout << "Ошибка открытия файла input.txt" << endl;
        return 1;
    }
    for (int i = 0; i < n; i++) {
        fin >> arr[i];
    }
    fin.close();
    
    // Сортировка Шелла по возрастанию с подсчётом обменов
    int swaps = 0;
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j = i;
            while (j >= gap && arr[j - gap] > temp) {
                arr[j] = arr[j - gap];
                j -= gap;
                swaps++;          // каждый сдвиг считаем как шаг (обмен)
            }
            arr[j] = temp;
            // если temp не перемещался, обмена не было – swaps не увеличивается
        }
    }
    
    // Запись результата в файл
    ofstream fout("output.txt");
    if (!fout) {
        cout << "Ошибка открытия файла output.txt" << endl;
        return 1;
    }
    for (int i = 0; i < n; i++) {
        fout << arr[i] << " ";
    }
    fout.close();
    
    // Вывод количества обменов
    cout << "Количество обменов при сортировке Шелла: " << swaps << endl;
    
    return 0;
}