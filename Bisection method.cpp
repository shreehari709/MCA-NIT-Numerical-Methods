//1)Wap to find the root of a equation using bisection method
//2)Wap to read and print students details using oops concepts 
//3)Wap to find sum and average of given n numbers using pointer and malloc function

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
double f(double x) {
    return pow(x, 3) - 7 * pow(x, 2) + 14 * x - 6;
}

int main() {

    double a = 0.0;
    double b = 1.0;
    double tolerance = 0.01; 
    double c;


    if (f(a) * f(b) >= 0) {
        cout << "The Bisection Method cannot be applied as f(a) and f(b) have the same sign." <<endl;
        return 1;
    }

    cout << fixed <<setprecision(4);
    cout << "Iteration\t a\t\t b\t\t c\t\t f(c)" << endl;

    int iteration = 0;
    while ((b - a) / 2.0 > tolerance) {
        c = (a + b) / 2.0; 
        
        cout << iteration++ << "\t\t " << a << "\t " << b << "\t " << c << "\t " << f(c) << endl;

        if (f(c) == 0.0) {
            break; 
        } else if (f(c) * f(a) < 0) {
            b = c; 
        } else {
            a = c; 
        }
    }

    cout << "\nThe root is approximately: " << c << " with tolerance: " << tolerance << endl;

    return 0;
}