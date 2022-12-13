def exists_word(word, instance):
    finds = list()
    lines = list()
    for item in range(len(instance)):
        count = 0
        test = instance.search(item)
        for line in test['linhas_do_arquivo']:
            count += 1
            if word.lower() in line.lower():
                lines.append({'linha': count})

    model = {
            "palavra": word,
            "arquivo": test['nome_do_arquivo'],
            "ocorrencias": lines
        }
    if lines == []:
        return []
    finds.append(model)
    return finds


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
