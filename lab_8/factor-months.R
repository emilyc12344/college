#!/usr/bin/Rscript

v <- c("March","April","January","November","January","September","October",
"September","November", "August","February",
"January","November","November","February","May","August","February",
"July","December","August","August","September","November","September",
"February","April")

print('Original vector')
print(v)

l <- c('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
fv <- factor(v, levels = l, ordered = TRUE)

print('Ordered factors of the said vector:')
print(fv, quote = FALSE)

print('Summary')
print(summary(fv))
