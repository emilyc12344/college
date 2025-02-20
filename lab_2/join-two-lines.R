#!/usr/bin/Rscript

input <- file('stdin', 'r')

l1 <- readLines(input, n=1)
l2 <- readLines(input, n=1)

paste(l1, l2)