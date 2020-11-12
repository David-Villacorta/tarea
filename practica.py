def division (a,b):
    cociente=0
    while a > 0:
        a=a-b
        if a >= 0:
            cociente=cociente+1
    return cociente

def modulo (x,y):
    mod=x-division(x,y)*y
    return mod

def capicua (n):
    if n == n[::-1]:
        return "capicua"
    else:
        return "no es capicua"

def base (a,b):
    c=0
    exp=0
    while a > 0:
        if b<10:
            x=modulo(a,b)
            a=division(a,b)
            c=c+x*10**exp
            exp=exp+1
    return c

# INICIO DE SESION

# USUARIO:simurdiera
# CONTRASEÑA:qwerty1234

con=0
usuario = input("INGRESE NOMBRE DE USUARIO: ")
contraseña = input("INGRESE LA CONTRASEÑA: ")
while usuario != "simurdiera" or con != contraseña:
    print("\n!!!EL USUARIO O CONTRASEÑA SON INCORRECTOS!!!")
    usuario = input("\nINGRESE NOMBRE DE USUARIO: ")
    contraseña = input("INGRESE LA CONTRASEÑA: ")
    a=0
    b=3
    con=[]
    for i in range (len(contraseña)-2):
        nuevo=contraseña[a:b]
        con.append(nuevo)
        con.extend(contraseña)
        con.reverse()
        a=a+1
        b=b+1
    contraseña=['4', '3', '2', '1', 'y', 't', 'r', 'e', 'w', 'q', '234', '4', 
    '3','2', '1', 'y', 't', 'r', 'e', 'w', 'q', 'y12', '4', '3', '2', '1', 'y', 
    't', 'r', 'e', 'w', 'q', 'rty', '4', '3', '2', '1', 'y', 't', 'r', 'e',
    'w', 'q', 'wer', 'qwe', 'q', 'w', 'e', 'r', 't', 'y', '1', '2', '3', '4',
    'ert', 'q', 'w', 'e', 'r', 't', 'y', '1', '2', '3', '4', 'ty1', 'q', 'w',
    'e', 'r', 't', 'y', '1', '2', '3', '4', '123', 'q', 'w', 'e', 'r', 't', 'y',
    '1', '2', '3', '4']

# MENU
opcion = 0
while opcion != 5:
    a=0
    b=0
    n=0
    print("\n######################")
    print("   MENU DE OPCIONES   ")
    print("######################")

    print("+--------------------+")
    print("| 1. DIVISION        |")
    print("| 2. DIVISORES       |")
    print("| 3. NUMEROS CAPICUA |")
    print("| 4. CAMBIO DE BASE  |")
    print("| 5. SALIR           |")
    print("+--------------------+\n")
    
    opcion = int(input("INGRESE LA OPCION QUE DESEA REALIZAR: "))
    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
        opcion = int(input("INGRESE LA OPCION QUE DESEA REALIZAR: "))

# DIVISION DE DOS NUMEROS
    if opcion == 1:
        a = int(input("\nINGRESE EL DIVIDENDO "))
        b = int(input("INGRESE EL DIVISOR "))
        if b==0:
            print("ERROR no es posible realizar la division entre 0")
        else:
            print("+------------------------------------+")
            print("EL COCIENTE ES",division(a,b),"Y EL RESIDUO ES",modulo(a,b))
            print("+------------------------------------+")
        continuar=input("\npresione INTRO para continuar")

# DIVISORES
    elif opcion == 2:
        divisores=[]
        while a <= 99999999999999:
            a=int(input("\nINGRESE UN NUMERO MAYOR A 99999999999999 "))
        for i in range(1,a+1):
            if modulo(a,i)==0:
                divisores.append(i)
        print("\nESTOS SON SUS DIVISORES:",divisores)
        continuar=input("\npresione INTRO para continuar") # puse esta opcion porque no me gustaba que el menu saliera con la respuesta

# CAPICUA
    elif opcion == 3:
        a=0
        b=3
        n=0
        while n <= 99999999:
            n=int(input("\nINGRESE UN NUMERO MAYOR A 99999999: "))
        print("\n+---------------------------+")
        n=str(n)
        for i in range (len(n)-2):
            nuevo=n[a:b]
            print(nuevo,"----------",capicua(nuevo))
            a=a+1
            b=b+1
        print("+---------------------------+")
        continuar=input("\npresione INTRO para continuar")

# CAMBIO DE BASE
    elif opcion == 4:
        b=10
        a=int(input("\nINGRESE EL NUMERO: "))
        while b >= 10:
            b=int(input("\nINGRESE LA BASE MENOR A 10: "))
        print("\n+-----------------------+")
        print(a,"EN BASE",b,"ES",base(a,b))
        print("+-----------------------+")
        continuar=input("\npresione INTRO para continuar")

# SALIR
print("+-----------------------+")
print("| GRACIAS VUELVA PRONTO |")
print("+-----------------------+")
