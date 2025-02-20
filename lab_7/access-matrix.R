#!/usr/bin/Rscript

print('Original Matrix')

A = matrix(seq(1, 16, by = 1), ncol = 4, byrow = TRUE)
colnames(A) = c('col1', 'col2', 'col3', 'col4')
rownames(A) = c('row1', 'row2', 'row3', 'row4')

print(A)

print('Access the element at 3rd column and 2nd row:')
print(A[2, 3])

print('Access only the  3rd row:')
print(A[3,])

print('Access only the 4th column:')
print(A[,4])
