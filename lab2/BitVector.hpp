#include <iostream>
#include <vector>

// I know this is inefficient and likely incorrect.
class BitVector {
 public:
  size_t size() const { return bits.size(); }
  bool operator[](size_t i) const { return bits[i]; }
  void push_back(bool b) { bits.push_back(b); }

  BitVector operator&(const BitVector& other) const {
    const BitVector& smaller = size() < other.size() ? *this : other;
    const BitVector& larger = size() < other.size() ? other : *this;
    BitVector result;
    for (size_t i = 0; i < smaller.size(); i++) {
      result.push_back(smaller[i] && larger[i]);
    }
    for (size_t i = smaller.size(); i < larger.size(); i++) {
      result.push_back(false);
    }
    return result;
  }

  BitVector operator|(const BitVector& other) const {
    const BitVector& smaller = size() < other.size() ? *this : other;
    const BitVector& larger = size() < other.size() ? other : *this;
    BitVector result;
    for (size_t i = 0; i < smaller.size(); i++) {
      result.push_back(smaller[i] || larger[i]);
    }
    for (size_t i = smaller.size(); i < larger.size(); i++) {
      result.push_back(larger[i]);
    }
    return result;
  }

  BitVector operator^(const BitVector& other) const {
    const BitVector& smaller = size() < other.size() ? *this : other;
    const BitVector& larger = size() < other.size() ? other : *this;
    BitVector result;
    for (size_t i = 0; i < smaller.size(); i++) {
      result.push_back(smaller[i] != larger[i]);
    }
    for (size_t i = smaller.size(); i < larger.size(); i++) {
      result.push_back(larger[i] ^ false);
    }
    return result;
  }

  friend std::ostream& operator<<(std::ostream& os, const BitVector& bv) {
    for (size_t i = 0; i < bv.size(); i++) {
      os << (bv[i] ? 1 : 0);
    }
    return os;
  }

 private:
  std::vector<bool> bits;
};

BitVector operator"" _bv(const char* s, size_t n) {
  BitVector bv;
  for (size_t i = 0; i < n; i++) {
    bv.push_back(s[i] == '1');
  }
  return bv;
}