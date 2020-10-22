### Miller-Rabin Test:
  Consider n be odd positive integer and we can write n -1 = (2^k)q where q is odd.
  Miller-Rabin witness is an integer a such that gcd(a, n) = 1. The following two conditions must be satisfied: 
    a^q is not congruent to 1 (mod n)
    a^((2^i)q) is not congruent to -1(mod n) for all i in the range of 0 to k-1
### Elliptic Curve Primality test
  So theorem states: Let n>1 be a natural number and there exists an element a in Z/nZ, s > 0 such that a^s = 1 is satisfied. We can write a^(s/q)-1 is in (Z/nZ)* for every prime divisor q of s. Then any prime that divides n is congruent to 1(mod s). Thus if s > sqrt(n), then n is a prime number.
http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=E87EF6128A3218BD77A47B05C157CA5D?doi=10.1.1.170.9116&rep=rep1&type=pdf
### Pratt Certificate
- based on Fermat's little theorem converse
- quick to generate for small numbers compared to other primality certificates
- n, positive integer
- p_i, set of prime factors of n-1
- There exists an int, x, that is the witness, such that x^(n-1) is congruent to 1 (mod n) but x^e is not congruent to 1 (mod n) where e, the list of (n-1)/p_i
- Fermat's little theorem states n is prime.
For example. Let n = 7919
n-1 = 7918 and p_i = {2,37,107}. 7 is a witness for 7919. So, 7^7918 is congruent to 1 (mod 7919).
Let a = 7918/2, b = 7918/37, c= 7918/107, and we see 7^a, 7^b, 7^c are not congruent to 1(mod 7919).
2 is a self-witness (prime without question) and rest are shown in a nested tree.
https://mathworld.wolfram.com/PrattCertificate.html
### Solovay-Strassen Test

### Pocklington- Theorem
- certification/deterministic
Let n - 1 =FR, F is the factored part of a number.
F = p_1^(a_1)*...*p_r^(a_r), 
where gcd(R,F) = 1 and R < sqrt(n). The test states that if there exists a b_i for i=1,...,r such that 
(b_i)^(n-1) is congruent 1 (mod n) and gcd((b_i)^((n-1)/p_i) - 1, n) = 1, then n is prime. 
https://mathworld.wolfram.com/PocklingtonsTheorem.html
### Baillie -PSW primality test
- composite
-influence of both Fermat's and Miller-Rabin test
Steps:
- process all N < 3 and all N that are even
- check N for any small prime divisors p < 1000
- perform a Miller-Rabin test, on base 2, N
- perform a Lucas-Selfridge test on N
https://faculty.lynchburg.edu/~nicely/misc/bpsw.html
