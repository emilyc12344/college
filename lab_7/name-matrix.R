#!/usr/bin/Rscript

print('Original Matrix')

A = matrix(seq(1, 16, by = 1), ncol = 4, byrow = TRUE)
colnames(A) = c('col1', 'col2', 'col3', 'col4')
rownames(A) = c('row1', 'row2', 'row3', 'row4')

print(A)
