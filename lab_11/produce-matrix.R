#!/usr/bin/Rscript

a <- matrix(rep(NA), ncol = 5, nrow = 5)
#print(a)

for (y in c(1:nrow(a))){
    for (x in c(1:ncol(a))){
        if (x == 1){
            a[y, x] <- y
        }
        else if (x == 2){
            if (y == 2){
                a[y, x] <- 1
            }
            else if (y > 2){
                a[y, x] <- 2
            }
            else {
                a[y, x] <- 0
            }
        }
        else if (x == 3){
            if (2 <= y  && y <= 4){
                a[y, x] <- 1
            }
            else if (y == 5) {
                a[y, x] <- 2
            }
            else {
                a[y, x] <- 0
            }
        }
        else {
            if (y < 3) {
                a[y, x] <- 0
            }
            else {
                a[y, x] <- 1
            }
        }
    }
}

print(a)
