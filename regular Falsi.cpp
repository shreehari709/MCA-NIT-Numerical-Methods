#include <iostream>
#include <cmath>
using namespace std;
double f(double x) {
    return 3 * x * x * x - 2 * x - 5; 
}

void regulaFalsi(double a, double b, double tolerance, int maxIterations) {
    if (f(a) * f(b) >= 0) {
        cout << "The initial guesses do not bracket the root." << endl;
        return;
    }

    double c; 
    int iteration = 0;

    cout << "Iteration\ta\t\tb\t\tc\t\tf(c)" << endl;
    do {      
        c = (a * f(b) - b * f(a)) / (f(b) - f(a));
        cout << iteration + 1 << "\t\t" << a << "\t\t" << b << "\t\t" << c << "\t\t" << f(c) << endl;

   
        if (fabs(f(c)) < tolerance) {
            break;
        }

        if (f(a) * f(c) < 0) {
            b = c;
        } else {
            a = c;
        }

        iteration++;
    } while (iteration < maxIterations);

    cout << "The root is approximately: " << c << endl;
}
int main() {
    double a, b, tolerance;
    int maxIterations;

    cout << "Enter the lower bound (a): ";
    cin >> a;
    cout << "Enter the upper bound (b): ";
    cin >> b;
  
	tolerance=0.01;
   maxIterations=10;

    regulaFalsi(a, b, tolerance, maxIterations);
    return 0;
}
