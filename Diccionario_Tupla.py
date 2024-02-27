
categorias = tuple((
    "Pan",
    "Postres",
    "Quesos",
    "Bebidas calientes"))

print("Bienvenido a nuestra panaderia")
print("Aca tenemos diferentes categorias")
print("Echales un vistaso")

for i, val in enumerate(categorias):
    print(f""" {i}, {val}""")

print("")

categoria1 = int(input())

print("")

if categoria1 == 0:
    
    pan = tuple((
        "Baguette",
        "Pan de molde",
        "Ciabatta",
        "Pan integral",
        "Pan pita",
        "Pan de centeno",
        "Bollos suizos",
        "Pan de avena",
        "Fougase",
        "Pretzel",
        "Promocion 4x1000 de pan de molde",
        "Promocion 3x7000 baguette"))

    precios_1 = ((
        3000,
        300,
        3000,
        350,
        3500,
        4000,
        500,
        450,
        4000,
        3000,
        1000,
        7000))
    for i, val in enumerate(pan):
        print(f""" {i}, {val} ${precios_1[i]}""")  
    opcion = int(input())
    print("")
    print(f"""Usuario usted ha seleccionado el producto {pan[opcion]} con un valor de ${precios_1[opcion]}""")
    print("")
    print("Usuario que cantidad de prodicto requiere? ")
    print("")

    cantidad_1 = int(input())
    print("")
    valor_1 = precios_1[opcion]*cantidad_1
    print("El nuevo valor es $", valor_1)
    
    print("")
    dinero = int(input("Ingrese el dinero: "))
    vueltos = dinero - valor_1
    print("")
    
    if dinero >= valor_1:
        print(f"Sus vueltos son ${vueltos} ")
    else:
        print(f"le falta un total de ${-vueltos}")
    
elif categoria1 == 2:
    
    quesos = tuple((
        "Brie",
        "Gouda",
        "Chedar",
        "Roquefort",
        "Parmesano",
        "Gorgonzola",
        "Camembert",
        "Mozzarella",
        "Emmental",
        "Manchego",
        "Promocion 3x7500 gouda",
        "Promocion 3x15000 Camembert"))

    precios_3 = ((
        3500,
        4500,
        3000,
        3500,
        2500,
        5500,
        6000,
        5500,
        3500,
        4500,
        7500,
        15000))
    for i, val in enumerate(quesos):
        print(f""" {i}, {val} ${precios_3[i]}""")  
    opcion = int(input())
    print("")
    print(f"""Usuario usted ha seleccionado el producto {quesos[opcion]} con un valor de ${precios_3[opcion]}""")
    print("")
    print("Usuario que cantidad de prodicto requiere? ")
    print("")

    cantidad_3 = int(input())
    print("")
    valor_3 = precios_3[opcion]*cantidad_3
    print("El nuevo valor es $", valor_3)
    
    print("")
    dinero = int(input("Ingrese el dinero: "))
    vueltos = dinero - valor_3
    print("")
    
    if dinero >= valor_3:
        print(f"Sus vueltos son ${vueltos} ")
    else:
        print(f"le falta un total de ${-vueltos}")

elif categoria1 == 1:
    
    postres = tuple((
        "Tiramiú",
        "Pastel de chocolate",
        "Cheesecake",
        "Helado de vainilla",
        "Profiteroles",
        "Mousse de mango",
        "Creepes con crema y fruta",
        "Flan",
        "Tarta de manzana",
        "Brownies",
        "Promocion 4x10000 Brownie",
        "Promocion 4x20000 Creepes con crema y fruta"))

    precios_2 = ((
        3000,
        4500,
        2500,
        3500,
        4000,
        5500,
        6000,
        3500,
        4000,
        3000,
        10000,
        20000))
    for i, val in enumerate(postres):
        print(f""" {i}, {val} ${precios_2[i]}""")  
    opcion = int(input())
    print("")
    print(f"""Usuario usted ha seleccionado el producto {postres[opcion]} con un valor de ${precios_2[opcion]}""")
    print("")
    print("Usuario que cantidad de prodicto requiere? ")
    print("")

    cantidad_2 = int(input())
    print("")
    valor_2 = precios_2[opcion]*cantidad_2
    print("El nuevo valor es $", valor_2)
    
    print("")
    dinero = int(input("Ingrese el dinero: "))
    vueltos = dinero - valor_2
    print("")
    
    if dinero >= valor_2:
        print(f"Sus vueltos son ${vueltos} ")
    else:
        print(f"le falta un total de ${-vueltos}")

elif categoria1 == 3:
    
    bebidas_calientes = tuple((
        "Cafe",
        "Chocolate caliente",
        "Capuchino",
        "Latte",
        "Espresso",
        "Te chai",
        "Cafe americano",
        "Mocha",
        "Cafe corto",
        "Te",
        "Promocion cafe y mocha "
        "Promocion te cahi y te"))

    precios_4 = ((
        3000,
        4500,
        2500,
        3500,
        4000,
        5500,
        6000,
        3500,
        4000,
        3000,
        6000,
        7000))

    for i, val in enumerate(bebidas_calientes):
        print(f""" {i}, {val} ${precios_4[i]}""")  
    opcion = int(input())
    print("")
    print(f"""Usuario usted ha seleccionado el producto {bebidas_calientes[opcion]} con un valor de ${precios_4[opcion]}""")
    print("")
    print("Usuario que cantidad de prodicto requiere? ")
    print("")

    cantidad_4 = int(input())
    print("")
    valor_4 = precios_4[opcion]*cantidad_4
    print("El nuevo valor es $", valor_4)
    
    print("")
    dinero = int(input("Ingrese el dinero: "))
    vueltos = dinero - valor_4
    print("")
    
    if dinero >= valor_4:
        print(f"Sus vueltos son ${vueltos} ")
    else:
        print(f"le falta un total de ${-vueltos}")
