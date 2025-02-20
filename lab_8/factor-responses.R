#!/usr/bin/Rscript

r <- factor(c("Agree", "Agree", "Strongly Agree", "Disagree","Agree"))

print('Original')
print(r)

print('Updated')
l <- c('Strongly Agree', 'Agree', 'Disagree', 'Strongly Disagree')
r <- factor(r, levels = l)
print(r)
