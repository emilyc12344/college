#!/usr/bin/Rscript

name = c('Brian', 'Sam', 'Penny', 'Conor', 'Ciaran', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jay')
score = c(14.5, 15, 12.5, 4.0, 3.0, 20.0, 13.5, 9.5, 8, 19)
attempts = c(1, 4, 2, 5, 2, 3, 3, 2, 1, 1)
qualify = c("yes","yes","yes","no","no","yes","yes","no","no","yes")

df <- data.frame(name = name, score = score, attempts = attempts, qualify = qualify)

print('Original Data Frame:')
print(df)

new <- data.frame(name = c('Patrick', 'Rebecca'), score = c(10, 15.4), attempts = c(2, 1), qualify = c('no', 'yes'))
print('Data Frame to be added')
print(new)

print('After adding new rows(s)')
rbind(df, new)
