import os
import zipfile

root = "BACKUP SEF II 09.2012 A 09.2019"

pastas = os.listdir(root)
# print (pastas)

for pasta in pastas:
    subpastas = [
        f
        for f in os.listdir(os.path.join(root, pasta))
        if not os.path.isfile(os.path.join(root, pasta, f))
    ]  # os.listdir(os.path.join(root, pasta))
    # print(subpastas)
    for subpasta in subpastas:
        pastas_data = [
            f
            for f in os.listdir(os.path.join(root, pasta, subpasta))
            if not os.path.isfile(os.path.join(root, pasta, subpasta, f))
        ]  # os.listdir(os.path.join(root, pasta, subpasta))
        # print(pastas_data)
        for pasta_data in pastas_data:
            pastas_zip = [
                f
                for f in os.listdir(os.path.join(root, pasta, subpasta, pasta_data))
                if os.path.isfile(os.path.join(root, pasta, subpasta, pasta_data, f))
            ]
            # print(pastas_zip)
            for file in pastas_zip:
                zip_teste = zipfile.ZipFile(
                    "zips_para_importar/"
                    + root
                    + "_"
                    + pasta
                    + "_"
                    + subpasta
                    + "_"
                    + pasta_data
                    + ".zip",
                    "a",
                )
                print(file)
                zip_teste.write(
                    os.path.join(root, pasta, subpasta, pasta_data, file),
                    file,
                    compress_type=zipfile.ZIP_DEFLATED,
                )

                zip_teste.close()
