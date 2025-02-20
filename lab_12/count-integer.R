#!/usr/bin/Rscript

f.count <- function(v, f) {
    count <- 0
    for (n in v) {
        if (n == f) {
            count <- count + 1
        } 
    }
    print(count)
}

#f.count(c(1:9, rep(10, 100)), 10)
