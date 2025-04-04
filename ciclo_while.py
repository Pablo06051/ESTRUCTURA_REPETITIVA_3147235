# imprimir la tabla de multiplicar 
# que el usuario ponga en el teclado
# usando el ciclo while 

numero = int(input("ingrese su numero: "))
i=10
while i >= 1: 
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
    ##insttruccion de
    ##incremento
    i = i - 1 

