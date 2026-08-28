#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <iomanip>
#include <cmath>
#include <clocale>

using namespace std;
using namespace chrono;

const int SIZE = 100;
const double MIN_VAL = -500.0;
const double MAX_VAL = 500.0;

// Генерация случайного вещественного числа в диапазоне [min, max]
double randomDouble(double min, double max) {
    return min + (double)rand() / RAND_MAX * (max - min);
}

// 1. Пузырьковая сортировка (Bubble sort)
void bubbleSort(vector<double>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

// 2. Сортировка Шелла (Shell sort)
void shellSort(vector<double>& arr) {
    int n = arr.size();
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            double temp = arr[i];
            int j = i;
            while (j >= gap && arr[j - gap] > temp) {
                arr[j] = arr[j - gap];
                j -= gap;
            }
            arr[j] = temp;
        }
    }
}

// 3. Быстрая сортировка (Quick sort)
int partition(vector<double>& arr, int low, int high) {
    double pivot = arr[high];
    int i = low - 1;
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSortRecursive(vector<double>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSortRecursive(arr, low, pi - 1);
        quickSortRecursive(arr, pi + 1, high);
    }
}

void quickSort(vector<double>& arr) {
    quickSortRecursive(arr, 0, arr.size() - 1);
}

// Измерение времени выполнения сортировки
double measureTime(vector<double> arr, void (*sortFunc)(vector<double>&)) {
    auto start = high_resolution_clock::now();
    sortFunc(arr);
    auto end = high_resolution_clock::now();
    duration<double> elapsed = end - start;
    return elapsed.count();
}

int main() {
    setlocale(LC_ALL, "ru_RU.UTF-8");
    srand(static_cast<unsigned>(time(nullptr)));

    // Генерация исходного массива
    vector<double> original(SIZE);
    for (int i = 0; i < SIZE; i++) {
        original[i] = randomDouble(MIN_VAL, MAX_VAL);
    }

    cout << "Размер массива: " << SIZE << endl;
    cout << "Диапазон: [" << MIN_VAL << ", " << MAX_VAL << "]\n" << endl;

    // Измерение времени трёх сортировок на копиях одного массива
    double timeBubble = measureTime(original, bubbleSort);
    double timeShell  = measureTime(original, shellSort);
    double timeQuick  = measureTime(original, quickSort);

    cout << fixed << setprecision(6);
    cout << "Время пузырьковой сортировки:  " << timeBubble << " сек" << endl;
    cout << "Время сортировки Шелла:        " << timeShell  << " сек" << endl;
    cout << "Время быстрой сортировки:      " << timeQuick  << " сек" << endl;

    // Проверка корректности (сортируем копию и проверяем порядок)
    vector<double> test = original;
    quickSort(test);
    bool sorted = true;
    for (size_t i = 1; i < test.size(); i++) {
        if (test[i-1] > test[i]) { sorted = false; break; }
    }
    cout << "\nСортировка выполнена корректно: " << (sorted ? "да" : "нет") << endl;

    return 0;
}