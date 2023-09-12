import temperatura as temp
import tiempo as time
import masa

def convertir_temperatura(valor, unidad_origen, unidad_destino):

    if unidad_origen == "celsius" and unidad_destino == "fahrenheit":
        return temp.cels_faher(valor)
    
    if unidad_origen == "fahrenheit" and unidad_destino == "celsius":
        return temp.faher_cels(valor)
    
    
def convertir_masa(valor, unidad_origen, unidad_destino):

    if unidad_origen == "kilogramos" and unidad_destino == "gramos":
        return masa.kgramos_Gramos(valor)
    
    if unidad_origen == "gramos" and unidad_destino == "kilogramos":
        return masa.gramos_kgramos(valor)
    
    
def convertir_tiempo(valor, unidad_origen, unidad_destino):

    if unidad_origen == "minutos" and unidad_destino == "segundos":
        return time.min_sec(valor)
    
    if unidad_origen == "segundos" and unidad_destino == "minutos":
        return time.sec_min(valor)
    
    
if __name__ == "__main__":

    condicion_bucle = True

    while condicion_bucle:

        seleccion_magnitud= input("¿Que magnitud de medida desea calcular?: ").lower()

        if seleccion_magnitud == "temperatura":
            uninidad_de_origen1 = input("ingrese la medida primer medida (celsius o fahrenheit): ")
            unidad_de_destino1 = input("ingrese la medida segunda medida (celsius o fahrenheit): ")
            valor= int(input("Ingrese el valor: "))
            convercion = convertir_temperatura(valor, uninidad_de_origen1.lower(), unidad_de_destino1.lower())
            print(f"{valor} de grados {uninidad_de_origen1} son equivalentes a {convercion} grados {unidad_de_destino1}")


        if seleccion_magnitud == "masa":
            unidad_de_origen2 = input("ingrese la medida primer medida (kilogramos o gramos): ")
            unidad_de_destino2= input("ingrese la medida segunda medida (kilogramos o gramos): ")
            valor = int(input("Ingrese el valor: "))
            convercion = convertir_masa(valor, unidad_de_origen2.lower(), unidad_de_destino2.lower())
            print(f"{valor} de {unidad_de_origen2} son equivalentes a {convercion} de {unidad_de_destino2}")


        if seleccion_magnitud == "tiempo":
            unidad_de_origen3 = input("ingrese la medida primer medida (minutos o segundos): ")
            unidad_de_destino3 = input("ingrese la medida segunda medida (minutos o segundos): ")
            valor = int(input("Ingrese el valor: "))
            convercion = convertir_tiempo(valor, unidad_de_origen3.lower(), unidad_de_destino3.lower())
            print(f"{valor} de {unidad_de_origen3} son equivalentes a {convercion} de {unidad_de_destino3}")
            

        opcion = input("¿Desea continuar? (si o no): ").lower()

        if opcion == "si":
            condicion_bucle = True
        
        elif opcion == "no":
            print("Gracias por ver :D")
            condicion_bucle = False
