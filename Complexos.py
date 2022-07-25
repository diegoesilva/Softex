#Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python. O método deve:

#- calcular três números complexos;
#- realizar todas as operações básicas;
#- e imprimir as propriedades real e img do números. 


def soma(real_1, imag_1, real_2, imag_2, real_3, imag_3): #soma
    a = complex(real_1, imag_1)
    b = complex(real_2, imag_2)
    c = complex(real_3, imag_3)
    return a+b+c


def subt(real_1, imag_1, real_2, imag_2, real_3, imag_3): #subtração
    a = complex(real_1, imag_1)
    b = complex(real_2, imag_2)
    c = complex(real_3, imag_3)
    return a-b-c

def mult(real_1, imag_1, real_2, imag_2, real_3, imag_3): #multiplicação
    a = complex(real_1, imag_1)
    b = complex(real_2, imag_2)
    c = complex(real_3, imag_3)
    return a*b*c

def div(real_1, imag_1, real_2, imag_2, real_3, imag_3): #divisão
    a = complex(real_1, imag_1)
    b = complex(real_2, imag_2)
    c = complex(real_3, imag_3)
    return a/b/c

def prop(real, imag): #propriedades
    a = complex(real, imag)
    print("Parte real = ", a.real)
    print("Parte imaginária = ", a.imag)


