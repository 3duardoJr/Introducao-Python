print('\n')
print("#----------Exercícios 5----------#")

def ler_graus():
    celsi = float(input("Informe a temperatura atual em graus celsius: "))
    return celsi

def conv_fahrenheit(c):
    temp_fahren = (9 * c + 160)/5
    return temp_fahren

def result(temp_fahren, temp_c):
    print(f"{temp_c}° em fahrennheit é {temp_fahren}")

temp_c = ler_graus()
temp_fahren = conv_fahrenheit(temp_c)
result(temp_fahren, temp_c)
