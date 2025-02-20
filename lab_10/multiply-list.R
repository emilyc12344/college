#!/usr/bin/Rscript

l <- list(v1 = 1:10, v2 = 'R Programming', v3 = 'XML')

print('Original list:')
print(l)

l$v1 <- l$v1 * 15

print('New list - First Element:')
print(l$v1)
