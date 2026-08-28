#include <iostream>
#include <clocale>

using namespace std;

// Рекурсивная функция проверки, является ли число степенью пятёрки
bool isPowerOfFive(int n) {
    if (n == 1)           // 5^0 = 1
        return true;
    if (n % 5 != 0 || n <= 0)
        return false;
    return isPowerOfFive(n / 5);
}

int main() {
    setlocale(LC_ALL, "ru_RU.UTF-8");
    
    int N;
    cout << "Введите натуральное число N: ";
    cin >> N;
    
    if (isPowerOfFive(N))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    
    return 0;
}