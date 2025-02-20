#!/usr/bin/env Rscript
input <- file('stdin', 'r')

x <- as.numeric(readLines(input,n=1))
y <- as.numeric(readLines(input,n=1))
z <- as.numeric(readLines(input, n=1))

if (x + y > z && x + z > y && y + z > x){
  print('yes')
} else {
  print('no')
}