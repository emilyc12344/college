#!/usr/bin/Rscript

x <- c(2, 4)
n <- 5

while (length(x) < 16) {
    if (n %% 2 == 0){
        x <- c(x, n)
    }
    n <- n + 1
}

print(x)
