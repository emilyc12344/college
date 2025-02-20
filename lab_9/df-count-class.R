#!/usr/bin/Rscript

name <- c('Amy', 'Lilly', 'George', 'Martin', 'Margret', 'Luke', 'Rebecca')
a <- c(25, 31, 23, 52, 76, 49, 26)
h <- c(173, 165, 185, 175, 161, 183, 165)
w <- c(47, 63, 93, 70, 78, 81, 55)
g <- c('F', 'F', 'M', 'M', 'F', 'M', 'F')
work <- c('Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes')
A <- data.frame(Age = a, Height = h, Weight = w, Gender = g)
B <- data.frame(Working = work)
C <- cbind(A, B)
rownames(C) <- name

print('Number of Rows')
print(nrow(C))

print('Number of Columns')
print(ncol(C))

print('Class of Data for C')
sapply(C, class)
