import xml.etree.ElementTree as ET

with open(r"/home/rcontrerasa/Escritorio/REDES_V/REPASOEV1/inventario.xml", "r") as arch:
    root = ET.parse(arch).getroot()

while True:
        
    print("""
        MENU
    1) LISTAR CATEGORIAS
    2) EXPLORAR CATEGORIA
    3) BUSCAR PRODUCTO POR ID
    4) SALIR
        """)
    opc = input("Seleccione: ")

    if opc == "1":
        print("Categorias Disponibles")
        for cat in root:
            print(f"- {cat.attrib["nombre"]}")
    elif opc == "2":
        busc = input("Categoria Buscada: ")
        for cat in root:
            if cat.attrib["nombre"] == busc:
                for product in cat:
                    print("="*20)
                    print(f"ID: [{product.attrib["id"]}]")
                    for data in product:
                        print(f"{data.tag}: {data.text}")
    elif opc == "3":
        busc_id = input("Ingresa ID: ")
        for cat in root:
            for product in cat:
                if product.attrib["id"] == busc_id:
                    for data in product:
                        print(f"{data.tag}: {data.text}")
    elif opc == "4":
        break
    else:
        print("x")
        