#!/usr/bin/Rscript

Emp <- function() {
    df <- data.frame(Name=c("ALAN S","RYAN S","SERAH S", "CHRISTY S","THOMAS MARTIN"),
        Gender=c("Male","Male","Female","Female","Male"),
        Age=c(23,22,25,26,32),
        Designation=c("Clerk","Manager","Executive","CEO","CTO"),
        SSN=c("134-34-2345","349-44-789","556-34-443","898-98-987","679-67-676"))
    return (df[c('Name', 'Age', 'Designation')])
}
