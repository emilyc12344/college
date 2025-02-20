#!/usr/bin/Rscript

m1 = matrix(seq(1, 12, by = 1), ncol = 3)
m2 = matrix(seq(13, 24, by = 1), ncol = 3)

print('Matrix-1')
print(m1)

print('Matrix-2')
print(m2)

print('After concatenating two given matrices:')
nm  = rbind(m1, m2)
print(nm)

print('Dimensions of New Matrix')
print(dim(nm))
