#!/usr/bin/Rscript

x <- c(1, 2, 3)
y <- c(4, 5, 6)
z <- c(7, 8, 9)

m <- matrix(cbind(x, y, z), ncol = 3)
rownames(m) <- c('a', 'b', 'c')
colnames(m) <- c('x', 'y', 'z')

v <- seq(1, 12, by = 1)
m2 <- matrix(v, ncol = 3, nrow = 4)
rownames(m2) <- c('a', 'b', 'c', 'd')
colnames(m2) <- c('x', 'y', 'z')

m2 <- t(m2)

print('Matrix Multiplication:')
print(m %*% m2)
