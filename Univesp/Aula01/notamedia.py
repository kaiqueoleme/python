c = 0
s = 0
nota = []
while c < 4:
    i = input("Digite um número: ")
    nota.append(i)
    c += 1

for n in nota:
    s += int(n)

m = s / len(nota)

if m >= 5:
    print("Aluno Aprovado com média ", m)
else:
    print("Aluno Reprovado com média ", m)
