#!/usr/bin/Rscript

n <- as.numeric(readLines('stdin'))

if (n >= 2 && (n == 2 || n %% 2 != 0) && (n == 3 || n %% 3 != 0) && (n == 5 || n %% 5 != 0)){
  print('prime')
} else  {
  print('not prime')
}