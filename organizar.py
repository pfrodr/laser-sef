import os
import shutil

import regex as re

import funcoes as fun

pastas = os.listdir("BACKUP SEF II 09.2012 A 09.2019")
print(pastas)

for pasta in pastas:
    pasta_processar = "BACKUP SEF II 09.2012 A 09.2019/" + pasta
    qtd_max_pasta = 20
    contador = 1

    try:
        os.mkdir(pasta_processar + "/data")
        print("pasta /data criada em " + pasta_processar)
    except FileExistsError:
        # print('pasta data/ já existe em ' + pasta_processar)
        pass

    with open(pasta_processar + "/INDICE.xml", encoding="ISO-8859-1") as xml:
        xml_string = xml.read()
        xml_final = "</Arquivos></Body></Indice>"
        xml_items = sorted(re.findall("<Arquivo>[\s\S]*?</Arquivo>", xml_string))
        xml_header = re.findall(".*?<Arquivos>", xml_string)
        files = [
            f
            for f in os.listdir(pasta_processar)
            if os.path.isfile(os.path.join(pasta_processar, f))
        ]
        pasta_atual = pasta_processar + "/data/" + str(contador)
        try:
            os.mkdir(pasta_atual)
        except FileExistsError:
            pass

        for f in files:
            if not f.endswith(".xml") and not f.endswith(".zip"):
                qtd_arquivos_pasta = fun.qtd_arquivos(pasta_atual)

                if qtd_arquivos_pasta < qtd_max_pasta:
                    shutil.copyfile(
                        os.path.join(pasta_processar, f), os.path.join(pasta_atual, f)
                    )
                elif qtd_arquivos_pasta == qtd_max_pasta:
                    with open(
                        pasta_atual + "/INDICE.xml", "w", encoding="ISO-8859-1"
                    ) as indice:
                        indice.write(
                            xml_header[0]
                            + "".join(xml_items[0:qtd_arquivos_pasta])
                            + xml_final
                        )
                    xml_items = xml_items[qtd_arquivos_pasta:]

                    contador = contador + 1

                    pasta_atual = pasta_processar + "/data/" + str(contador)

                    try:
                        os.mkdir(pasta_atual)
                    except FileExistsError:
                        pass

                    shutil.copyfile(
                        os.path.join(pasta_processar, f), os.path.join(pasta_atual, f)
                    )

        with open(pasta_atual + "/INDICE.xml", "w", encoding="ISO-8859-1") as indice:
            indice.write(
                xml_header[0]
                + "".join(xml_items[0 : fun.qtd_arquivos(pasta_atual)])
                + xml_final
            )
        xml_items = xml_items[fun.qtd_arquivos(pasta_atual) :]
