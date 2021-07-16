import os, csv, sys

#####################################

#A dificldade nessa questão está no fato que houveram compras
#distintas no mesmo dia e é necessário diferenciá-las...

#Leremos o arquivo com as DIVERGÊNCIAS e em seguida faremos outro arquivo
#Que irão constar todos os itens defeituosos e seus preços/datas.



#######################################
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

os.chdir('C:\\Users\\paulo\\Documents\\GitHub\\VF_CARDOSO_MARTINS\\Questão 1\\Compras')
directory = os.path.join("C:\\Users\\paulo\\Documents\\GitHub\\VF_CARDOSO_MARTINS\\Questão 1\\Compras")

with open('TODOS_ARQUIVOS_COM_DATA', "w") as myfile:   ##SERVE PARA ZERAR O ARQUIVO EM CADA ITERAÇÃO
    newData = ''
    myfile.write(newData)
with open('DIVERGENCIAS_DE_PRECO', "w") as myfile:
    newData = ''
    myfile.write(newData)

for root,dirs,files in os.walk(directory):
                        
    for file in files:       
       if file.endswith(".csv"):                      
           f = open(file, 'r')
           data = f.readlines()           
           g=open("TODOS_ARQUIVOS_COM_DATA",'a')
           
           for line in data:
               atributos_itens_separados = line.split(",")
               g.write(atributos_itens_separados[0]+','+atributos_itens_separados[1]+','+atributos_itens_separados[2])                
           g.close()
           f.close()
           

contador = -1
contador_auxiliar = -1
preço_1 = -1
preço_2 = -1
h = open('TODOS_ARQUIVOS_COM_DATA', 'r')
dados = h.readlines()

for line in dados:

    contador = contador + 1
    atributos_comparativos = line.split(",")
    nome_1 = atributos_comparativos[0]
    preço_1 =float(atributos_comparativos[1])
    data_1 = atributos_comparativos[2]    
    for line_auxiliar in dados:
        contador_auxiliar = contador_auxiliar + 1
        atributos_comparativos_auxiliares = line_auxiliar.split(',')
        nome_2 = atributos_comparativos_auxiliares[0]
        preço_2 = float(atributos_comparativos_auxiliares[1])
        data_2 = atributos_comparativos_auxiliares[2]
        if contador_auxiliar > contador:
            if (preço_1/1.25>preço_2 and nome_1 == nome_2):                
                print("Preço_1:"+str(preço_1)+'\n')
                print("Preço 2:"+str(preço_2)+'\n')
                l=open("DIVERGENCIAS_DE_PRECO",'a')
                l.write(nome_1+','+str(preço_1)+','+data_1+nome_2+','+str(preço_2)+','+data_2+'\n')
                l.close()
            if (preço_2/1.25>preço_1 and nome_1 == nome_2):
                l = open("DIVERGENCIAS_DE_PRECO", 'a')
                l.write(nome_1+','+str(preço_1)+','+data_1+nome_2+','+str(preço_2)+','+data_2+'\n') 
                l.close() 

    contador_auxiliar = -1

h.close()


m = open('DIVERGENCIAS_DE_PRECO', 'r')
n = open('TODOS_ARQUIVOS_COM_DATA', 'r')
    

m.close()
n.close()