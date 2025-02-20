#!/usr/bin/Rscript

l1 <- c('Red', 'Green', 'Blue')
l2 <- matrix(c(1, 3, 5, 7, 9, 11), nrow = 2)
l3 <- list('Python', 'C', 'Java')

l <- list(l1, l2, l3)
names(l) <- c('Colour', 'Odd Numbers', 'Languages')

print('List')

l[[length(l) + 1]] = 'New element'
print(l)
