import os
os.system("cls, clear")

def isfloat(f: str) -> bool:
    string_float = True
    simbolos = "-+.,"
    for i in range(len(f)):
        if not f[i].isnumeric or not f[i] in simbolos:
            string_float = False

    return string_float

print(isfloat("345"))
print(isfloat("34.5"))
print(isfloat("34,5"))
print(isfloat("34."))
print(isfloat("-34.5"))
print(isfloat("A34.5"))