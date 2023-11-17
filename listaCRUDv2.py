#para cada -invitado-(que serÃ¡ la clase) se debe almacenar nombre y apellido
#Segunda verion usando clases y listas

print('Este programa es un CRUD')  

class invitado:
    def __init__(self, nombre, apellido): 
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def setNombre(self, pnombre):
        self.nombre = pnombre
    def setApellido(self, papellido):
        self.apellido = papellido
        
def agregar():
    nombre = input("ingrese nombre: ").capitalize()
    apellido = input("ingrese apellido: ").capitalize()
    invNuevo = invitado(nombre, apellido)
    listaInvitados.append(invNuevo) #append es el metodo para agregar un elemento a la lista
    
def ver():
    print("")
    print('LISTA DE INVITADOS'.center(30,"="))
                    
    for num in range(0, len(listaInvitados)):
        print(f"{num + 1} - {listaInvitados[num]}")
              
    print('FIN DE LA LISTA'.center(30,"="))
    print(" ")
    
def modificar():
    ver()
    modificar = int(input("Ingresa el número del invitado que desea modificar: "))
    nombre=input("Ingrese nuevo nombre: ").capitalize()
    apellido=input("Ingrese nuevo apellido: ").capitalize()
    listaInvitados[modificar - 1].setNombre(nombre)
    listaInvitados[modificar - 1].setApellido(apellido)
    
    
def borrar():
    ver()
    eliminar = int(input("Ingresa el número del invitado que desea eliminar: "))
    print(f"se va a eliminar {listaInvitados[eliminar -1].getNombre()} {listaInvitados[eliminar -1].getApellido()}")
    respuesta = input ("¿continuar? (si o no)")
    if respuesta.lower()=="si":
        listaInvitados.remove(listaInvitados[eliminar - 1])
    
    #lista = ["1", "2", "3"] una lista de characteres
    #lista.remove("1") se tiene que escribir el character para eliminar

def guardar():
    with open("invitados.txt","w") as lista:
       for num in range(0, len(listaInvitados)):
           lista.write(f"{num + 1} - {listaInvitados[num]}\n")
                 
       print("Se guardo la lista correctamente")  
    
    
listaInvitados=[]

#invitados iniciales de prueba
inv1 = invitado("Lucia", "Cortes")
inv2 = invitado("Luis", "Rodriguez")
inv3 = invitado("Jesus", "Rodriguez")
listaInvitados.append(inv1)
listaInvitados.append(inv2)
listaInvitados.append(inv3)

while True: 
    
    print("""_______________________
          Operaciones que puedes realizar:
          
    1 - Agregar nuevo invitado.
    2 - ver lista de invitados.
    3 - Modificar invitado.
    4 - Eliminar invitado.
    5 - Guardar lista.
    6 - SALIR.
  
    """)
    
    op = input("Ingresa el número de la operacion: ")
    if op == "1":
            while True:
                agregar()
                otro = input("¿desea agregar otro invitado? (si o no)")
                if otro.lower()=="si":
                    pass
                else:
                    break
                
    elif op == "2": 
        ver()      
                    
    elif op == "3":
        modificar()
                          
    elif op == "4":
        borrar()
  
    elif op == '5':
        guardar()
    
    elif op == '6':
        otro = input("¿Desea guardar los cambios antes de salir? (si o no)")
        if otro.lower()=="si":
            guardar()
            break
        else:
            break

    else:
        print('Comando invalido')
        break

print ("Ha finalizado el programa")    
