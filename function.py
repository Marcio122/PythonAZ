def sum(inp1, inp2):
    if type (inp1) == type(inp2):
        return inp1 + inp2
    else:
        return "Datatypes are different."
    
x = sum("Marcio", "Jeovety")
print(x)