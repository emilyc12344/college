#!/usr/bin/env Rscript
input <- file('stdin', 'r')

x <- as.numeric(readLines(input, n=1))
y <- as.numeric(readLines(input, n=1))
print(x * y)