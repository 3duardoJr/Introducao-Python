import re
print("\n")

dados = ''' 
            Número: (21)985864229
            Cep: 25090-55
            Url: https://www.sitepessoal.com.br
            Número: (21)985864229
            Cep: 25090-55
            Url: https://www.sitepessoal.com.br
            Número: (21)985864229
            Cep: 25090-55
            Url: https://www.sitepessoal.com.br
            Número: (21)985864229
            Cep: 25090-55
            Url: https://www.sitepessoal.com.br
        '''
#-------------------------------------------------
print(re.findall('\(\d{2}\)\d{8,9}', dados))
print("---")
print(re.findall('\d{5}-\d{2}', dados))
print("---")
print(re.findall('https?://[A-Za-z0-9./]+', dados))
