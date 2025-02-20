#!/usr/bin/Rscript

M <- matrix(seq(1, 16, by = 1), ncol = 4, nrow = 4, byrow = TRUE)
rownames(M) = c('row1', 'row2', 'row3', 'row4')
colnames(M) = c('col1', 'col2', 'col3', 'col4')

print('Original Matrix')
print(M)

s <- M[M[,3] > 8,]

print('New submatrix')
print(s)
