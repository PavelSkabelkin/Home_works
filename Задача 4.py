R1 = float(input("Введите сопротивление первого проводника: "))
R2 = float(input("Введите сопротивление второго проводника: "))

R_total = R1 + R2

R_total_rounded = round(R_total, 1)

print(f"Общее сопротивление цепи: {R_total_rounded}")