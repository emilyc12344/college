#!/usr/bin/Rscript

input <- file('stdin', 'r')

l1 <- readLines(input, n=1)
l2 <- readLines(input, n=1)

print(l2)
print(l1)