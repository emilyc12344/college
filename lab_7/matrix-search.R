#!/usr/bin/Rscript

m = matrix(seq(1, 16, by = 1), ncol = 4, byrow = TRUE)
rownames(m) = c('row1', 'row2', 'row3', 'row4')
colnames(m) = c('col1', 'col2', 'col3', 'col4')

print('Original Matrix')
print(m)

m[m > 10] <- 0

print('Modified Matrix:')
print(m)
