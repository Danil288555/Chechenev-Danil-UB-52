#include <iostream>
#include <cmath>
#include <clocale>
#include <iomanip>
#include <corecrt_math_defines.h>

using namespace std;

int main() {
    setlocale(LC_ALL, "ru_RU.UTF-8");   // для корректного вывода русских букв в VS Code

    double x1, x2, dx;
    const double eps = 0.0001;
    const double PI_2 = M_PI_2;         // π/2 из <cmath>

    cout << "Вычисление arctan(x) для x > 1 с помощью ряда Тейлора\n";
    cout << "Ряд: arctan(x) = π/2 - (1/x - 1/(3x^3) + 1/(5x^5) - ...)\n";
    cout << "Точность eps = " << eps << endl;

    // Ввод и проверка корректности
    do {
        cout << "\nВведите x1 и x2 (x1 > 1, x2 > 1, x1 < x2): ";
        cin >> x1 >> x2;
        cout << "Введите шаг dx (>0): ";
        cin >> dx;

        if (x1 <= 1.0 || x2 <= 1.0 || x1 >= x2 || dx <= 0) {
            cout << "Ошибка ввода! Повторите.\n";
        }
    } while (x1 <= 1.0 || x2 <= 1.0 || x1 >= x2 || dx <= 0);

    cout << fixed << setprecision(6);
    cout << "\n   x    |   arctan(x) (ряд)   |   atan(x) (библ.)   |  Погрешность\n";
    cout << "---------------------------------------------------------------\n";

    double x = x1;
    while (x <= x2 + 1e-9) {   // обход с учётом погрешности
        double S = 0.0;        // сумма ряда для arctan(1/x)
        double term = 1.0 / x; // первый член (n=0)
        int n = 0;
        while (fabs(term) > eps) {
            S += term;
            // рекуррентный переход к следующему члену
            term = -term / (x * x) * (2.0 * n + 1) / (2.0 * n + 3);
            n++;
        }
        double res = PI_2 - S; // arctan(x) = π/2 - S
        double y_lib = atan(x);
        double error = fabs(res - y_lib);

        cout << setw(6) << x << "   |   " << setw(15) << res << "   |   "
             << setw(15) << y_lib << "   |   " << setw(10) << error << endl;

        x += dx;
    }

    return 0;
}