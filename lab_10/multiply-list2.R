#!/usr/bin/Rscript

l1 <- list(1, 2, 3)
l2 <- list(4, 5, 6)

print('Original lists:')
print(l1)
print(l2)

v1 <- unlist(l1)
v2 <- unlist(l2)

print('Convert the lists to vectors:')
print(v1)
print(v2)

print('Multiply vectors:')
print('New Vector:')
print(v1 * v2)
