# Evelyn Victoria
# 07/05/2024

# Cálculo Bhaskara

import math

a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))
c = float(input("Digite um valor para c: "))


delta = b**2 - 4*a*c

if delta < 0:
    print("Raízes não reais")
elif delta == 0:
    x = -b / (2*a)
    print(x)
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print(x1, x2)



