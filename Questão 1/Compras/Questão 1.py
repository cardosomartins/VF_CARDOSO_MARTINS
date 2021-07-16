import os, csv, sys


# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

os.chdir('C:\\Users\\paulo\\Documents\\GitHub\\VF_CARDOSO_MARTINS\\Questão 1\\Compras')
directory = os.path.join("C:\\Users\\paulo\\Documents\\GitHub\\VF_CARDOSO_MARTINS\\Questão 1\\Compras")


with open('TODOS_ARQUIVOS_SEM_DATA', "w") as myfile:
    newData = ''
    myfile.write(newData)

for root,dirs,files in os.walk(directory):
    
    for file in files:       
       if file.endswith(".csv"):                      
           f = open(file, 'r')
           data = f.readlines()           
           g=open("TODOS_ARQUIVOS_SEM_DATA",'a')
           
           for line in data:
               atributos_itens_separados = line.split(",")
               g.write(atributos_itens_separados[0]+','+atributos_itens_separados[1]+'\n')                 
           g.close()
           f.close()
           print(file + ' foi analisado')