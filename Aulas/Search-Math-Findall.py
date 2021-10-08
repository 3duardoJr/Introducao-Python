import re
print("\n")

celular = 'Meu número de contato é (21)98586-4229 ... (21)98586-4229'
placa = 'FrT-509'
email = "O email de contato é edu.ferreira.s.j@gmail.com"
email2 = "edu.ferreira.s.j@gmail.com é meu email de contato"
# --------------------------------------------------------
print("#----------Search----------#")
print(re.search('\(\d{2}\)\d{4,5}-\d{4}', celular))
print("---")
print(re.search('[A-Za-z]{3}-\d{3}', placa))
print("---")
print(re.search('.+@\w+\.com', email))
print("----------------------------")
print("\n")
print("#-----------Match-----------#")
print(re.match('.+@\w+\.com', email2))  # Para encontra no inicio de alguma string
print("-----------------------------")
print("\n")
print("#----------Findall----------#")
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', celular))  # Para encontrar todas as strings do mesmo padrão
print("-----------------------------")
