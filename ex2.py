x = str(input("Digite seu texto: ")).upper()
c = x.count("A")
if c > 0:
    print(f"A letra 'A' aparece {c} vezes")
else:
    print("Não contem nenhuma letra 'A'")
