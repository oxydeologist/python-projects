#nCr Calculator by oxydeologist
import math
n = int(input("Please type in n: "))
r = int(input("Please type in r: "))
n_factorial = math.factorial(n)
r_factorial = math.factorial(r)
n_minus_r = n - r
nr_factorial = math.factorial(n_minus_r)
nCr = n_factorial / (r_factorial * nr_factorial)
print(nCr)

# I JUST REALISED YOU CAN DO math.comb*n,r) AHAHAHAHHA
