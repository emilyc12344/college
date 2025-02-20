#!/usr/bin/env Rscript
input <- file('stdin', 'r')

x <- as.numeric(readLines(input,n=1))

if (x %% 3 == 0 && x %% 5 == 0){
  print('fizz-buzz')
} else if (x %% 3 == 0){
  print('fizz')
} else if (x %% 5 == 0){
  print('buzz')
} else {
  print(x)
}