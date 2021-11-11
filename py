Python

Másodfokú egyenlet.

print("Van-e megoldasa a masodfoku egyenletnek?")

a = int(input("kérem az a együtthatot:"))
b = int(input("kérem a b együtthatot:"))
c = int(input("kérem a c együtthatot:"))

diszkriminans = b*b - 4*a*c

if diszkriminans == 0:
    print("Az egyenletnek egy megoldasa van.")
else:
    if diszkriminans < 0:
        print("Az egyenletnek nincs megoldasa.")
    else:
        print("Az egyenletnek kétmegoldasa van.")

   
        
        
