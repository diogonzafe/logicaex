n = int(input("Digite um número: "))

a, b = 0, 1
pertence = False
while a <= n:
    if a == n:
        pertence = True
        break
    a, b = b, a + b

if pertence:
    print(f"O número {n} pertence a sequência.")
else:
    print(f"O número {n} NÃO pertence a sequência.")