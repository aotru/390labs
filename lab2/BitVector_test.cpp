#include "BitVector.hpp"

#include <iostream>

using namespace std;

int main() {
  cout << "101010"_bv << endl;

  BitVector a = "100100100"_bv;
  BitVector b = "11001110011"_bv;

  cout << (a & b) << endl;
  cout << (a | b) << endl;
  cout << (a ^ b) << endl;

  a.push_back(true);
  a.push_back(false);
  a.push_back(false);
  for (size_t i = 0; i < a.size(); i++) {
    cout << a[i] << endl;
  }
}
