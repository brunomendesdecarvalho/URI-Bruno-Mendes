# coding: utf-8

# entradas:

N1, N2, N3, N4 = input().split(" ")
nota_exame = 0
media_final = 0
# computações:

N1, N2, N3, N4 = float(N1), float(N2), float(N3), float(N4)
media_ponderada = (2*N1 + 3*N2 + 4*N3 + N4)/10
print('Media: %.1f' % media_ponderada)

# Saídas:

if(media_ponderada >= 7.0):
    print('Aluno aprovado.')

elif(media_ponderada < 5.0):
    print('Aluno reprovado.')

elif(5.0 <= media_ponderada < 7.0):
    print('Aluno em exame.')
    nota_exame = float(input())
    media_final = (nota_exame + media_ponderada)/2
    print('Nota do exame: %.1f' % nota_exame)

    if (media_final >= 5.0):
        print('Aluno aprovado.')
        print('Media final: %.1f' % media_final)

    else:
        print('Aluno reprovado.')
        print('Media final: %.1f' % media_final)
