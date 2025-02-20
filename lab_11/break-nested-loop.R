#!/usr/bin/Rscript

for (a in 1:5){
    for (b in 1:5){
        if (b <= 2){
            print(c(a, b))
        }
        else {
            break
        }
    }
}
