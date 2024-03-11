#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    // FOR loops - known amount of looping
    cout << "[FOR LOOPS]\n";
    cout << "Event numbers: ";

    for (int i = 0; i < 10; i++) {
        if (i % 2) continue; // continue loop if odd number
        cout << i << "; ";
    }


    // WHILE loops - unknown amount of looping
    cout << "\n\n[WHILE LOOPS]\n";

    int num = 1234;
    cout << "Chars from " << num << ": ";

    while (num != 0) {
        cout << num % 10 << "; ";
        num /= 10;
    }


    const int a = 0, b = 10;
    int curr, max, ran;
    cout << "\nGenerating random even number from <" << a << "; " << b << ">: ";

    srand(time(0));

    max = 2;
    curr = 0;

    do {
        if (curr >= max) {
            cout << "Reached limit (" << max << ")";
            break;
        }

        ran = rand() % (b - a) + a;
        curr++;
    } while (ran % 2);

    if (!(ran % 2)) {
        cout << ran << "; found after " << curr << " search(es)";
    }

    return 0;
}