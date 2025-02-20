#!/usr/bin/env Rscript
input <- file('stdin', 'r')

x <- readLines(input,n=1)
y <- readLines(input,n=1)

if (nchar(x) > nchar(y)) {
  print(x)
} else {
  print(y)
}