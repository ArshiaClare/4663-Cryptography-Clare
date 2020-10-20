### Miller-Rabin Test:
  Consider n be odd positive integer and we can write n -1 = (2^k)q where q is odd.
  Miller-Rabin witness is an integer a such that gcd(a, n) = 1. The following two conditions must be satisfied: 
    a^q is not congruent to 1 (mod n)
    a^((2^i)q) is not congruent to -1(mod n) for all i in the range of 0 to k-1
  Error:
### Elliptic Curve Primality test
  So theorem states: Let n>1 be a natural number and there exists an element a in Z/nZ, s > 0 such that a^s = 1 is satisfied. We can write a^(s/q)-1 is in (Z/nZ)* for every prime divisor q of s. Then any prime that divides n is congruent to 1(mod s). Thus if s > sqrt(n), then n is a prime number.
