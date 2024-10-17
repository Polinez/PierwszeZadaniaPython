
# zad 1
temperature=int(input("Podaj temperature w Kelwinach: "))
lNeutronow=int(input("Podaj liczbe neutronow na sekunde: "))

def is_criticality_balanced(temperature, lNeutronow):
    if temperature<800 or lNeutronow>500 or temperature*lNeutronow<500000:
        return True
    else :
        return False

print(is_criticality_balanced(temperature, lNeutronow))