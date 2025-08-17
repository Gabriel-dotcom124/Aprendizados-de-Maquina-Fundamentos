Atributos numéricos são aqueles que apresentam valores discretos (int) ou contínuos (float) para representar quantidades. Em geral, modelos trabalham melhor com dados com escalas reduzidas, ou seja, a escala do atributo é transformada para o intervalo entre  [−1,1] ,  [0,1]  etc.


data[['math', 'reading', 'writing']]


Escalaa
  Normalização


min =  data['math'].min()
print(min)

max = data['math'].max()
print(max)

data['math_norm'] = data['math'].apply(lambda grade: (grade - min) / (max - min))


min = data['math_norm'].min()
print(min)

max = data['math_norm'].max()
print(max)


    Padronização


media = data['math'].mean()
print(media)

desvio_padrao = data['math'].std()
print(desvio_padrao)


data['math_padr'] = data['math'].apply(lambda nota: (nota - media) / desvio_padrao)


media = data['math_padr'].mean()
print(media)

desvio_padrao = data['math_padr'].std()
print(desvio_padrao)
