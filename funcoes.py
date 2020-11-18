import os


def qtd_arquivos(start_path):
    return len(
        [
            name
            for name in os.listdir(start_path)
            if os.path.isfile(os.path.join(start_path, name))
        ]
    )
