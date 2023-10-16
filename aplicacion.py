login = open("login.txt","rt")
leerLogin=login.read()

password= open("clave.txt","rt")
leerClave=password.read()

intentos=0
while intentos<2:
    user= input("Ingrese usuario: ")
    clave = input("Ingrese clave: ")
    if user==leerLogin and clave==leerClave:
        print("Datos Persona")
        print("1. Listar personas")
        print("2. Agregar Personas")
        print("3. Salir")
        intentos+=2
    else:
        print("Usuario y/o clave incorrectos")
        intentos+=1
        

