#!/usr/bin/Rscript

x <- as.numeric(readLines('stdin'))

if (x >= 5){
  print('weekend')
} else {
  print('weekday')
}