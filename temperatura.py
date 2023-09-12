def cels_faher(celsius):
    rest1 = (celsius *9/5) + 32
    return rest1

def faher_cels(fahrenheit):
    rest2 = (fahrenheit - 32) * 5/9
    return rest2

if __name__ == "__main__":
    cels_faher()
    faher_cels()