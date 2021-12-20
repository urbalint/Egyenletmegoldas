a = float (input ("első paraméter (a)?:"))
b = float (input ("második paraméter(b)?:"))

c = float (input ("Harmadik paraméter(c)?:"))
if a == 0:
    b = float (input ("első paraméter (a)?:"))
    c = float (input ("második paraméter(b)?:"))
    if b != 0:
        x = -c/b
        print("\tAz eredmény:",x)
    else:
        if c == 0:
            print("\tMinden megoldás")
        else:
            print("\tNincsen megoldás")


else:
    d = b*b - 4 * a * c
    if d >= 0:
        
        x1 = (-b + math.sqrt( b*b - 4 * a * c ) ) / (2 * a)
        x2 = (-b - math.sqrt( b*b - 4 * a * c ) ) / (2 * a)
        print("Az másodfokú egyenlet megoldása x1: ", x1 )
        print("Az másodfokú egyenlet megoldása x2: ", x2 )
    else:
        print("\tNincsen megoldása a valósszámok halmazán.")
        
