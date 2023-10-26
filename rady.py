# tento program rozdává rady do života

print("Odpovídej ano nebo ne")
stastna_retezec = input("jsi šťastná?")
if stastna_retezec == "ano" or stastna_retezec == "Ano":
    stastna = True
elif stastna_retezec == "ne" or stastna_retezec == "Ne":
    stastna = False
else:
    print("nerozumim!")

bohata_retezec = input("Jsi bohatá?")
if bohata_retezec == "ano" or bohata_retezec == "Ano":
    bohata = True
elif bohata_retezec == "ne" or bohata_retezec == "Ne":
    bohata = False
else:
    print("Nerozumím!")

if stastna and bohata:
    print("gratuluji!")
elif bohata:
    print("Zkus se víc usmívat!")
elif stastna:
    print("Zkus míň utrácet!")
else:
    print("To je mi líto!")

    print("hello world!") #tak ještě
