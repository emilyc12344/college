#!/usr/bin/Rscript

create.matrix <- function() {
    return (matrix(v, ncol = 4, byrow = TRUE))    
}

v <- scan(file('stdin', 'r'), what = 'character', nmax = 8, quiet = TRUE)
