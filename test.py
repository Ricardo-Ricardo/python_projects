xs = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
#print((filter(lambda x: 'abc-123' in x, xs)))
#print(list(filter(lambda x: 'abc-123' in x, xs)))



# Searching for “int”
if 'abc' in str(xs):
    print(xs.index("abc-123"))
else:
    print("none")
#Output - 1
