a = float (input ("első paraméter (a)?:"))
b = float (input ("második paraméter(b)?:"))
if a != 0:
    x = -b/a
    print("\tAz eredmény:",x)
else:
    if b == 0:
        print("\tMinden megoldás")
    else:
        print("\tNincsen megoldás")
