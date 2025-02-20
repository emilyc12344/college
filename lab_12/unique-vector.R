#!/usr/bin/Rscript

f.uniq <- function(v) {
    new <- c()
    for (n in v) {
        if (n %in% new) {
            n <- n
        } else {
            new <- c(new, n)
        }
    }
    print(new)
}

#f.uniq(c(9, 9, 1, 1, 0))
