import sys


def txt_importer(path_file):
    try:
        if path_file.endswith('.txt'):
            result = list()
            with open(path_file, 'r') as file:
                for line in file:
                    result.append(line.rstrip())
            return result
        else:
            print(sys.stderr.write('Formato inválido\n'))
    except FileNotFoundError:
        print(sys.stderr.write(f'Arquivo {path_file} não encontrado\n'))
