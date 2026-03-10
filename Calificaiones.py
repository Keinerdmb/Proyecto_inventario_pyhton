#----Sistema de cálculo de promedio por módulo en RIWI----

#----VARIABLES----

coders = 0
suma_promedios = 0
reprobados = 0
regulares = 0
excelentes = 0
mejor_promedio = -1
mejor_coder = ""

#----FUNCIONES----

def pedir_nota(frente):
    while True:
        try:
            nota = float(input(f"ingrese la nota de {frente} (0-100):"))
            if 0 <= nota <= 100:
                return nota
            else:
                print("La nota debe estar entre 0 y 100")
        except ValueError:
            print("Debe ingresar un número valido")

def mostrar_resumen(modulo, coders, suma_promedios, reprobados, regulares, excelentes, mejor_coder, mejor_promedio):
    print("\n" + "="*30)
    print(f"Resumen del módulo: {modulo}")
    print("="*30)
    print(f"Total de coders registrados: {coders}")
    if coders > 0:
        print(f"Promedio general del grupo: {suma_promedios / coders: .2f}")
    print(f"Reprobados: {reprobados}")
    print(f"Regulares: {regulares}")
    print(f"Excelentes: {excelentes}")
    print(f"Mejor coder: {mejor_coder} con promedio {mejor_promedio: .2f}")
    print("="*30 + "\n")
    input("Presione ENTER para finalizar...")
   





#----PROGRAMA----

print("Bienvenido \n")

while True: 
    try:
        modulo = int(input("Ingrese el número del modulo: \n"))
        break   
    except ValueError:
        print("\nError: Ingrese un modulo valido\n")  
    

while True:
    nombre = input("\nIngresa el nombre del coder:")

    desarrollo = pedir_nota("\nDesarrollo de software")   
    socioemocional = pedir_nota("Habilidades socioemocionales")
    ingles = pedir_nota ("Inglés\n")

    promedio = (desarrollo * 0.6) + (socioemocional * 0.2) + (ingles * 0.2)

    print("\nCoder:", nombre)
    print("Módulo:", modulo)
    print("Promedio:", promedio)

    if promedio < 50:
        print("Clasificación: Reprobado")
        reprobados += 1
    elif promedio < 80:
        print("Clasificación: Regular")
    else:
        print("Clasificación: Excelente")

    if desarrollo < 50:
        print("Observación: Debe reforzar el frente técnico principal")        

    coders = +1
    suma_promedios += promedio

    if promedio > mejor_promedio:
        mejor_promedio = promedio 
        mejor_coder = nombre        

    continuar = input("¿Registrar otro coder? (s/n):")
    if continuar.lower() != "s":
        break

    #----RESUMEN----

    mostrar_resumen(modulo, coders, suma_promedios, reprobados, regulares, excelentes, mejor_coder, mejor_promedio)


           
