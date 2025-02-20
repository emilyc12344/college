#!/usr/bin/Rscript

name = factor(c('Brian', 'Sam', 'Penny', 'Conor', 'Ciaran', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jay'))
score = c(14.5, 15, 12.5, 4.0, 3.0, 20.0, 13.5, 9.5, 8, 19)
attempts = c(1, 4, 2, 5, 2, 3, 3, 2, 1, 1)
qualify = factor(c("yes","yes","yes","no","no","yes","yes","no","no","yes"))

df <- data.frame(name = name, score = score, attempts = attempts, qualify = qualify)

print('Column Names:')
print(colnames(df))

print('Row Names:')
print(rownames(df))

print('Initial Rows')
print(head(df))

print('New Row Names:')
rownames(df) <- c("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th")
print(rownames(df))
