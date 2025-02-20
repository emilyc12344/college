#!/usr/bin/Rscript

input <- file('stdin', 'r')

a <- as.numeric(readLines(input, n=1))
b <- as.numeric(readLines(input, n=1))
c <- as.numeric(readLines(input, n=1))

if ((a ^ 2) == (b ^ 2) + (c ^ 2)){
  print(TRUE)
} else {
  print(FALSE)
}
