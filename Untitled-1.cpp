#include <iostream>

int main() {

    int n;

    std::cout << "Intronuceti valoarea lui n: ";

    std::cin >> n;

    std::cout << ( n >= 0 ? "Numarul este pozitiv!" : "Numarul etse negativ!") << std::endl;

    return 0;
}