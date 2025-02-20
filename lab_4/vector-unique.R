#!/usr/bin/Rscript

str =  c("The","quick","brown","fox","jumps","over","the","lazy","dog")
u_str = unique(tolower(str))
nums = c(1, 2, 2, 3, 4, 4, 5, 6)

print('Original vector(string)')
print(str)
print('Unique elements of the said vector:')
print(u_str)
      
print('Original vector(number)')
print(nums)
print('Unique elements of the said vector:')
print(unique(nums))