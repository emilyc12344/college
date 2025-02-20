#!/usr/bin/Rscript

user.read2 <- function() {
  values <- scan(file, what = "character", nmax = 10, quiet = TRUE)
    return(values)
}

file <- file('stdin', 'r')
