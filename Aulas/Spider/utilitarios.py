def soma(a, b ,c):
    result = a+b+c
    return result

def mult(a, b, c):
    result_m = a*b*c
    return result_m

def palindromo(string):
    if string == string[::-1]:
        return True
    else:
        return False
    