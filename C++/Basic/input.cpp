#include <iostream>
using namespace std;

int main() {
    const int year = 2023;
    int birth_year;

    cout << "Pass your birth year: ";
    cin >> birth_year;

    if (cin.fail() || birth_year < 1900 || birth_year > year) {
        cout << "Wrong Input";
        return 0;
    }

    cout << "You will be " << year - birth_year << " by the end of this year :]";
    return 0;
}