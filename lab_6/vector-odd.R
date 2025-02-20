#!/usr/bin/Rscript

v <- c(29,1,37,49,4,36,34,5,38,13)
z <- v %% 2 != 0
print(v[z])
