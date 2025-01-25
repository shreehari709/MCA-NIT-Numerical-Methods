//1)Wap to find the root of a equation using bisection method


/*#include <iostream>
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
}*/
//2)Wap to read and print students details using oops concepts 
/*
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int rollNumber;
    float marks;

public:
    void inputDetails() {
        cout << "Enter student name: "<<endl;
        cin>>name;
        cout << "Enter roll number: "<<endl;
        cin >> rollNumber;
        cout << "Enter marks: "<<endl;
        cin >> marks;
    }

    void displayDetails() const {
        cout << "\nStudent Details:" << endl;
        cout << "Name: " << name << endl;
        cout << "Roll Number: " << rollNumber << endl;
        cout << "Marks: " << marks << endl;
    }
};

int main() {
    int n;
    cout << "Enter the number of students: ";
    cin >> n;
    Student st[n];
    
    for (int i = 0; i < n; ++i) {
        cout << "\nEntering details for student " << i + 1 << ":" << endl;
        st[i].inputDetails();
    }


    cout << "\nDisplaying student details:" << endl;
    for (int i = 0; i < n; ++i) {
        st[i].displayDetails();
    }
    return 0;
}
*/
//3)Wap to find sum and average of given n numbers using pointer and malloc function
#include<iostream>
using namespace std;
int main(){
	int n,sum=0;
	cout<<"Enter the Number of Element = ";
	cin>>n;
	int* arr = (int*)malloc(n * sizeof(int));

	for(int i = 0; i<n;i++){
		cin>>arr[i];
		sum = *(arr+i)+sum;	
	}
	float avg = sum/n;
		cout<<"The Sum is = "<<sum<<endl;
		cout<<"The Avg is = "<<avg;
	return 0;
}