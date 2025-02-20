#!/usr/bin/Rscript

v <- c(45:41, 30:33)
b <- c('C', 'A', 'B', 'C', 'B', 'A', 'C', 'B', 'A')
n <- c(69, 61, 60, 69, 65, 60, 66, 68, 68)

df = data.frame(Age = v, Class = b, Grade = n)

print('Original DataFrame')
print(df)

print('DataFrame Ordered by Age')
print(df[order(df$Age), ])
