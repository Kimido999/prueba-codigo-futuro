def cels_faher(celsius):
    rest1 = (celsius *9/5) + 32
    return rest1

def faher_cels(fahrenheit):
    rest2 = (fahrenheit - 32) * 5/9
    return rest2

if __name__ == "__main__":
    cls = float(input("Ingrese su mediada en celsius: "))
    fhr = cels_faher(cls)
    print(f"{cls}°c equivalen a {fhr} fahrenheit")

    fhr2 = float(input("Ingrese su medida en Fahrenheit: "))
    cls2 = faher_cels(fhr2)
    print(f"{fhr2} fahrenheit equivalen a {cls2}°c")