from ast import Delete
from treelib import Node,Tree
from zookeeper import Ztree
from zookeeper import Znode 



arbol = Ztree()

while(True):
    print("\t\t-------Bienvenido a Zookeeper--------")
    print("*** Selecciona una opción *****")
    print("1. Crear Znode")
    print("2. Borrar Znode")
    print("3. Ver arbol")
    print("4. ver informacion de Znode")
    print("5. Cambiar Data de Znode")
    print("6. Mostrar hijos de Znode")
    print("7. Buscar Znodo")
    print("8. Ver data de Znode")
    print("0. Salir")

    opcion = input("$")

    if(opcion == "0"):
        break
    if(opcion == "1"):
        path = input("Path = ")
        data = input("Contenido de Znode = ")
        efimero = input("Es efimero? (True/False) =")
        onservice = input("El servidor esta activo? (True/False) =")
        deadtime = input("Deadtime =")
        padre = input("Ruta del padre =")
        if(efimero == "True"):
            efimero = True
        if(efimero == "False"):
            efimero = False
        if(onservice == "True"):
            onservice = True
        if(onservice == "False"):
            onservice = False
        arbol.create(path,data,efimero,onservice,int(deadtime),padre)
    if(opcion == "2"):
        path = input("Path = ")
        version = input("Version actual =")
        arbol.delete(path,int(version))
    if(opcion == "3"):
        arbol.showTree()
    if(opcion =="4"):
        path = input("Path = ")
        arbol.showNode(path)
    if(opcion == "5"):
        path = input("Path = ")
        contenido = input("Contenido =")
        arbol.setData(path,contenido)
    if (opcion=="6"):
        path = input("Path = ")
        print(arbol.getChildren(path))
    if (opcion=="7"):
        path = input("Path = ")
        if(arbol.exist(path)):
            print("Nodo encontrado")
        else:
            print("Nodo NO encontrado")
    if(opcion == "8"):
        path = input("Path = ")
        print(arbol.getData(path))
        




#arbol.create("/Amazon",{"hola",123,"soy data"},False,True,None,"/")
#arbol.create("/Nodo2",{"holiiiis"},True,True,120,"/")
#arbol.create("/Amazon/Nodo3",{},False,True,None,"/Amazon")
#arbol.create("/Amazon/Nodo4",{"contenido nuevo",2,"hey"},False,True,None,"/Amazon")
#arbol.create("/Amazon/Nodo5",{"contenido nuevo",2,"hey"},False,True,None,"/Amazon/Nodo3")
#arbol.showTree()

#arbol.delete("/Nodo2",0)
#print(arbol.getData("/Amazon"))
#arbol.setData("/Amazon",{"contenido nuevo",2,"hey"})
#arbol.showNode("/Amazon")
#arbol.getChildren("/Amazon")

