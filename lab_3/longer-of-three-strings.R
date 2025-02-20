#!/usr/bin/env Rscript
input <- file('stdin', 'r')

x <- readLines(input,n=1)
y <- readLines(input,n=1)
z <- readLines(input, n=1)

x1 = nchar(x)
y1 = nchar(y)
z1 = nchar(z)

if (x1 > y1 && x1 > z1) {
  print(x)
} else if (y1 > x1 && y1 > z1) {
  print(y)
} else {
  print(z)
}