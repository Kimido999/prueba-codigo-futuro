def kgramos_Gramos(kmasa):
    rest3 = kmasa * 1000
    return rest3

def gramos_kgramos(mmasa):
    rest4 = mmasa /1000
    return rest4

if __name__== "__main__":
    usk = float(input("Ingrese su masa en Kilogramos: "))
    masan = kgramos_Gramos(usk)
    print(f"{usk} kilogramos son {masan} gramos")

    usn = float(input("Ingrese su masa en Gramos: "))
    masak = gramos_kgramos(usn)
    print(f"{usn} gramos son {masak} kilogramos")
    