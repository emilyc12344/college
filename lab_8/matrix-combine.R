#!/usr/bin/Rscript

x <- c(1, 2, 3)
y <- c(4, 5, 6)
z <- c(7, 8, 9)

m <- matrix(cbind(x, y, z), ncol = 3)
rownames(m) <- c('a', 'b', 'c')
colnames(m) <- c('x', 'y', 'z')

print('Content of matrix one:')
print(m)
