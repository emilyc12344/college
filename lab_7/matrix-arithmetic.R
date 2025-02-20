#!/usr/bin/Rscript

m1 <- matrix(seq(1, 6, by = 1), ncol = 3)
m2 <- matrix(c(1, 2, 3, 1, 2, 3), ncol = 3)

print('Matrix-1:')
print(m1)

print('Matrix-2:')
print(m2)

print('Result of addition')
print(m1 + m2)

print('Result of subtraction')
print(m1 - m2)

print('Result of multiplication')
print(m1 * m2)

print('Result of division')
print(m1 / m2)
