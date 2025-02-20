#!/usr/bin/env Rscript
input <- file('stdin', 'r')

x <- as.numeric(readLines(input,n=1))
y <- as.numeric(readLines(input,n=1))

if (x == y){
  print('Draw.')
} else if (x > y){
  print('Home win.')
} else {
  print('Away win.')
}