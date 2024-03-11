#include <iostream>
using namespace std;

int main() {
    cout << "[ARRAY]";

    // After declaring array, you can't change it's size
    int size = 4;
    int example_array[size];

    int arr[] = { 1, 2, 3 };
    float arr_2[]{ 1.2, 8.4, -2.5 };
    string arr_3[]{ "Hello", "World!", "Test1234" };

    // Getting size of array
    cout << "Size of arr:";
    cout << "\n - " << sizeof(arr) / sizeof(arr[0]) << " elements";
    cout << "\n - " << sizeof(arr) << " bytes";
    cout << "\n - " << sizeof(arr[0]) << " bytes per element\n\n";

    // Getting and changing items
    arr[0] = 10;
    cout << "First element: " << arr[0]; // first element
    cout << "\nLast element: " << arr[sizeof(arr) / sizeof(arr[0]) - 1]; // last element: size - 1

    return 0;
}