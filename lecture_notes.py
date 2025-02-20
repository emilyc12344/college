from re import findall

s = 'cactcatcatctactacatcatcatcatcatacTCat'
p = r'[^Cc]at'
print(findall(p, s))

p = r'\D'
print(findall(p, s))

#r befor string - raw string (ignores \n?)
# [] in str - character class (put options e.g. cap and low)
# ^ in character class- without
# \D - non decimal char
# ^ - matches start of str
# $ - matches end of str
# \s - whitespace
# \b - word boundary
# \w - alpha numeric
# ? - char before is optional
# * - matches zero or more of char before
# + - one or more

s = 'duke of lamesville of'
p = r'\bof$'
print(findall(p, s))

s = 'And start with and'
p = r'^[Aa]nd\b'
print(findall(p, s))

s = 'colour or color'
p = r'[Cc]olou?r'
print(findall(p, s))

s = 'is this a date: 25-01-2034 or 25/02/25'
p = r'\d{2}[-/]\d{2}[-/]\d{2}'
print(findall(p, s))

s = 'March 17 or April 1'
p = r'(?:March|April) \d{1,2}'
print(findall(p, s))

s = 'ABcdegQWERTYUIOPxyzZASDF'
p = '[A-Z]+'
print(max(findall(p, s), key=len))
