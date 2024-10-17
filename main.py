
# Task 1

# temperature=int(input("Podaj temperature w Kelwinach: "))
# lNeutronow=int(input("Podaj liczbe neutronow na sekunde: "))

def is_criticality_balanced(temperature, lNeutronow):
    if temperature<800 or lNeutronow>500 or temperature*lNeutronow<500000:
        return True
    else :
        return False

# print(is_criticality_balanced(temperature, lNeutronow))


# Task 2
voltage=float(input("Podaj napiecie:"))
current=float(input("podaj aktualna:"))
theoretical_max_power=float(input("podaj teoretyczna maksymalna moc: "))

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency=(generated_power/theoretical_max_power)*100

    if efficiency>=80:
        return "zielony"
    elif efficiency>=60 and efficiency<80:
        return "pomaranczowy"
    elif efficiency>=30 and efficiency<60:
        return "czerwony"
    else: return "czarny"

print(reactor_efficiency(voltage,current,theoretical_max_power))






