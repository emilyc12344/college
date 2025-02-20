#!/usr/bin/Rscript

m <- matrix((24:39), nrow = 4, byrow=TRUE)
colnames(m) <- c('col1', 'col2', 'col3', 'col4')
rownames(m) <- c('row1', 'row2', 'row3', 'row4')

print('Original Matrix:')
print(m)

sub <- m[m >= 32, ncol=4]

print('New submatrix:')
print(sub)
