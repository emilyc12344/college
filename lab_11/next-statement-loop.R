#!/usr/bin/Rscript

i <- 1

while (i < 6){
    i <- i + 1
    if (i == 4){
        next
    }
    else {
        print(i)
    }
}
