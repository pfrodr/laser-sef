import os
import zipfile

pastas = os.listdir('BACKUP SEF II 09.2012 A 09.2019')
print (pastas)

for pasta in pastas:
    subpastas = os.listdir(pasta)


# zip_teste = zipfile.ZipFile('zips_para_importar/' + , 'w')
 
# for file in os.listdir('BACKUP SEF II 09.2012 A 09.2019/01/data/1'):
#     print(file)
#     zip_teste.write(os.path.join('BACKUP SEF II 09.2012 A 09.2019/01/data/1', file),  file, compress_type = zipfile.ZIP_DEFLATED)
 
# zip_teste.close()
