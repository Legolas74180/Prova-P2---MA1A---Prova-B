#Exercicio 1- Receber 2 parâmetros e retornar a média das duas notas.

def media(nota1,nota2):
    media=(nota1+nota2)/2
    return media


#Obs:Tentei de varias formas abrir o arquivo e não foi, não consegui dar continuidade nos outros exercicios pq dependia do exercicio 2.
listaNetflix=[]
serieAntiga=open('series.csv','r',encoding='utf-8')
serieNova=open('series_novas.csv','r',encoding='utf-8')
for line in serieAntiga.readlines():
    listaNetflix.append(line)
    serieAntiga.close()
for line2 in serieNova.readlines():
    listaNetflix.append(line2)
    serieAntiga.close()
print(listaNetflix)
#A lista da vazio...


