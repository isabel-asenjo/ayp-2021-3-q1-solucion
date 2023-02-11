def numeros_abundantes(ab_nums):
    # busco los números abundantes que existen entre un poco antes del precio mínimo (para poder hacer el descuento en ese caso también) y el precio máximo que se puede pagar en la clínica
    for num in range(15,131):
        divs = 0
        for d in range(1,num):
            if num%d == 0:
                divs += d
        if divs > num:
            ab_nums.append(num)

def registro(payments, pets):
    doctors = ['Angela Johnson', 'David Kane', 'Marcus Stewart', 'Jessica Cruz']

    services = [
        {
            "name": "Consulta",
            "price": 20,
        },
        {
            "name": "Operación",
            "price": 80,
        },
        {
            "name": "Peluquería",
            "price": 30,
        },
    ]

    pet_types = ["Perro", "Gato", "Pájaro"]


    # mostrar doctores
    print("\nSELECCIÓN DE DOCTOR:")
    for i,d in enumerate(doctors):
        print(f"{i+1}. {d}")

    # seleccionar doctor
    doc_index = input("Ingrese el número correspondiente al doctor que comenzará su turno >> ")
    while not doc_index.isnumeric() or int(doc_index) not in range(1,len(doctors)+1):
        print("Por favor, ingrese una opción válida.")
        doc_index = input(">> ")

    # pedir datos cliente
    print("\nDATOS DEL CLIENTE:")
    pet_name = input("Ingrese el nombre de la mascota >> ")
    while pet_name == " " or not pet_name.replace(" ","").isalpha():
        pet_name = input("Ingreso inválido. Ingrese el nombre de la mascota >> ")

    owner_dni = input("\nIngrese el DNI del dueño >> ")
    while not owner_dni.isnumeric() or int(owner_dni) == 0:
        owner_dni = input("Ingreso inválido. Ingrese el DNI del dueño >> ")

    # revisar si ya la mascota existe en la base de datos. Si no existe, se pide la otra info
    registered = False
    current_pet = {}
    for key,value in pets.items():
        if value['pet_name'] == pet_name.capitalize() and value['owner_dni'] == owner_dni:
            print("\nMascota ya existente en la base de datos. Se procederá a la selección de servicios.")
            registered = True
            current_pet = value
            break
    if not registered:
        pet_age = input("\nIngrese la edad de la mascota >> ")
        while not pet_age.isnumeric() or int(pet_age) == 0:
            pet_age = input("Ingreso inválido. Ingrese la edad de la mascota >> ")

        print("\n")
        for i,pt in enumerate(pet_types):
                print(f"{i+1}. {pt}")
        pet_type = input("Ingrese el número correspondiente al tipo de mascota >> ")
        while pet_type != "1" and pet_type != "2" and pet_type != "3":
            pet_type = input("Ingreso inválido. Ingrese el número correspondiente al tipo de mascota >> ")

        pet_breed = input("\nIngrese la raza de la mascota >> ")
        while pet_breed == " " or not pet_breed.replace(" ","").isalpha():
            pet_breed = input("Ingreso inválido. Ingrese la raza de la mascota >> ")
        
        owner_name = input("\nIngrese el nombre del dueño >> ")
        while owner_name == " " or not owner_name.replace(" ","").isalpha():
            owner_name = input("Ingreso inválido. Ingrese el nombre del dueño >> ")

        owner_phone = input("\nIngrese el número de teléfono del dueño >> ")
        while not owner_phone.isnumeric() or len(owner_phone) != 11:
            owner_phone = input("Ingreso inválido. Ingrese el número de teléfono del dueño >> ")

        # guardar info en diccionario
        current_pet = pets[len(pets)] = {
            'pet_name': pet_name.capitalize(),
            'pet_age': int(pet_age),
            'pet_type': pet_types[int(pet_type)-1],
            'pet_breed': pet_breed.capitalize(),
            'owner_name': owner_name.capitalize(),
            'owner_dni': owner_dni,
            'owner_phone': owner_phone,
        }


    # seleccionar servicios a adquirir
    selected_services = []
    while True:
        print("\n")
        for i,s in enumerate(services):
            print(f"{i+1}. {s['name']}: ${s['price']}")
        service = input("\nIngrese el número correspondiente al servicio a adquirir >> ")
        while service != "1" and service != "2" and service != "3":
            print("Por favor, ingrese una opción válida.")
            service = input(">> ")
        if services[int(service)-1] in selected_services:
            print("\nEste servicio ya fue adquirido.")
        else:
            selected_services.append(services[int(service)-1])
        
        more = input("\n¿Desea agregar otro producto? ('s' para 'sí', 'n' para 'no') >> ").lower()
        while more != 's' and more != 'n':
            print("Por favor, ingrese una opción válida.")
            more = input(">> ")
        
        if more == 'n':
            break

    # comenzar a imprimir factura
    print("\n--------RESUMEN DE COMPRA--------")
    print("DATOS DEL DOCTOR:")
    print(f"Doctor: {doctors[int(doc_index)-1]}")
    print("\nDATOS DE LA MASCOTA:")
    print(f"- Nombre: {current_pet['pet_name']}\n- Edad: {current_pet['pet_age']}\n- Tipo: {current_pet['pet_type']}\n- Raza: {current_pet['pet_breed']}")
    print("\nDATOS DEL DUEÑO:")
    print(f"- DNI: {current_pet['owner_dni']}\n- Nombre: {current_pet['owner_name']}\n- Teléfono: {current_pet['owner_phone']}")
    print("--------------------------------")

    # calcular descuento
    amnt_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    discount = 0
    total = 0
    ab_nums = []
    numeros_abundantes(ab_nums)

    print("DATOS DE LOS SERVICIOS:")
    for s in selected_services:
        print(f"- {s['name']}: ${s['price']}")
        total += s["price"]
    for char in pet_name:
        if char in vowels:
            amnt_vowels += 1
    if amnt_vowels >= 3:
        for i in range(len(ab_nums)):
            if i+1 < len(ab_nums):
                if ab_nums[i] < total and ab_nums[i+1] >= total:
                    discount = ab_nums[i]
            elif i == len(ab_nums)-1 and discount == 0:
                    discount = ab_nums[i]
    else:
        discount = total

    # terminar de imprimir factura
    print("--------------------------------")
    print(f"Precio sin descuento: ${total}\nPrecio con descuento: ${discount}")

    # guardar info del pago
    for key, value in pets.items():
        if value == current_pet:
            pet_index = key
            break
    payments.append((pet_index, pet_name.capitalize(), owner_dni, doctors[int(doc_index)-1], int(discount)))


def estadisticas(payments, pets):
    # mascotas que más van
    freq_pets = []
    pet_keys = [p[0] for p in payments] # guardo los keys que usé en el diccionario de mascotas para contar cuántas veces se repiten
    if len(pets) > 0:
        for key, value in pets.items():
            freq_pets.append([value['pet_name'], pet_keys.count(key)])

        freq_pets = sorted(freq_pets, key=(lambda freq_pets : freq_pets[1]), reverse=True)
        print("\nLAS 3 MASCOTAS QUE VIENEN CON MAYOR FRECUENCIA:")
        for i in range(len(freq_pets)):
            if i < 3:
                print(f"{i+1}. {freq_pets[i][0]}")
            else:
                break
    else:
        print("\nTodavía no hay mascotas registradas.")

    # owners con más mascotas
    owners = [value['owner_name'] for key,value in pets.items()]
    freq_owners = []
    if len(owners) > 0:
        for o in owners:
            freq_owners.append((o, owners.count(o)))
        freq_owners = list(set(freq_owners))
        freq_owners = sorted(freq_owners, key=(lambda freq_owners : freq_owners[1]), reverse=True)
        print("\nLOS 3 DUEÑOS CON MÁS MASCOTAS:")
        for i in range(len(freq_owners)):
            if i < 3:
                print(f"{i+1}. {freq_owners[i][0]}")
            else:
                break
    else:
        print("\nTodavía no hay mascotas registradas.")

    # pagos más altos
    if len(payments) > 0:
        sorted_payments = sorted(payments, key=(lambda payments : payments[4]), reverse=True)
        print("\nLOS 3 PAGOS MÁS ALTOS:")
        for i in range(len(sorted_payments)):
            if i < 3:
                print(f"{i+1}. {sorted_payments[i]}")
            else:
                break
    else:
        print("\nTodavía no hay pagos registrados.")


def main():

    pets = {}

    payments = []


    while True:
        print("¡Bienvenido a la clínica veterinaria! Seleccione una opción:\n1. Registrar transacción\n2. Ver estadísticas\n3. Salir")
        selection = input(">> ")
        while selection != "1" and selection != "2" and selection != "3":
            print("Por favor, ingrese una opción válida.")
            selection = input(">> ")
        
        if selection == "1":
            registro(payments, pets)

            print("\n")

        elif selection == "2":
            estadisticas(payments, pets)
            
            print("\n")

        else:
            print("¡Hasta luego!")
            break

main()