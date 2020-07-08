def succ(Z):
    return Z + 1
def pred(Z):
    if Z >= 1:
        return Z - 1
    else:
        return 0

""" Diferencia acotada de X e Y, guardando la solución en Z """
def pw(X1,X2,X3,X4):
    X3=succ(X1)
    X3=pred(X3)
    while X4!=X2:
        X3=pred(X3)
        X4=succ(X4)
    return X3

print(pw(5,3,0,0))
print(pw(3,5,0,0))