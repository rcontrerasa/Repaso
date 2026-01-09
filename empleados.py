#Empleados
import json

with open(r"/home/rcontrerasa/Escritorio/REDES_V/REPASOEV1/empleados.json", "r") as arch:
    datos = json.load(arch)
dep_list = datos["departamentos"]
while True:
        
    print("""
        MENU
    1) LISTAR EMPLEADOS
    2) BUSCAR EMPLEADO
    3) SALIR
        """)
    opc = input("Seleccione: ")

    if opc == "1":
        for dep in dep_list:
            print("="*25)
            print(f"Departamento: {dep["nombre"]}")
            print("="*25)
            for emp in dep["empleados"]:
                print(f"Nombre: {emp["nombre"]}")
                print(f"Puesto: {emp["puesto"]}")
                print("")
    elif opc == "2":
        
        busc = input("Que empleado Desea Buscar: ")
        for dep in dep_list:
            for emp in dep["empleados"]:
                if emp["nombre"] == busc:
                    print(f"Empleado: {emp["nombre"]}")
                    print("Habilidades: ", *emp["habilidades"])
    elif opc == "3":
        break
    else:
        print("Error.")
                  
