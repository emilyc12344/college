#!/usr/bin/Rscript

f1 <- c('a', 'b', 'c', 'd', 'e', 'd')
f2 <- c('a', 'b', 'b', 'e', 'a', 'c')

print('Original factors:')
print(factor(f1))
print(factor(f2))

print('After concatenate factor becomes:')
f3 <- c(f1, f2)
levels(f3) <- c(levels(f1), levels(f2))
print(factor(f3))
