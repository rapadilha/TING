from ting_file_management import file_management
import sys


def process(path_file, instance):
    file = file_management.txt_importer(path_file)
    model = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    for path in range(len(instance)):
        if path_file == instance.search(path)["nome_do_arquivo"]:
            return None
    instance.enqueue(model)
    print(model)


def remove(instance):
    try:
        remove = instance.dequeue()
        item = remove["nome_do_arquivo"]
        sys.stdout.write(f'Arquivo {item} removido com sucesso\n')
    except IndexError:
        sys.stdout.write('Não há elementos\n')

def file_metadata(instance, position):
    """Aqui irá sua implementação"""
