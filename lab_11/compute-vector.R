#!/usr/bin/Rscript

a <- c(15:20)
b <- c(10:5)
x <- c(15:20)
i <- 1

while (i < length(a) + 1) {
    l <- length(b) + 1 - i
    x[i] <- a[i] * b[l]
    i <- i + 1
}

print(x)
