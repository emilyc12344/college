#!/usr/bin/Rscript

v <- c(1, 2, 3, 3, 4, NA, 3, 2, 4, 5, NA, 5)

print('Original vector:')
print(v)

print('Levels of factor of the said vector:')
print(levels(factor(v)))
