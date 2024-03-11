#include <iostream>
using namespace std;

int main() {
    int x = 2;

    switch (x + 1) {
    case 1:
        cout << "cool";
        break;
    case 2:
        cout << "not cool";
        break;
    case 10:
        cout << "interesting";
        break;
    default:
        cout << "default";
        break;
    }

    return 0;
}