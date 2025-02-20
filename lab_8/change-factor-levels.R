#!/usr/bin/Rscript

v <- c('a', 'b', 'a', 'c', 'b')

print('Original vector:')
print(v)

print('Factor of the said vector:')
f <- factor(v)
print(f)
levels(f)[1] <- 'e'
print(f)
