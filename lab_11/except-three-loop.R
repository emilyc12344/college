#!/usr/bin/Rscript

i <- 1:5

for (n in i){
    if (n == 3){
        next
    }
    else {
        print(n)
    }
}
