import re


def tratarLista(string):
    regex = r'\d+\s+(.+)'
    nomes = re.findall(regex, string)
    nomes = [nome.strip() for nome in nomes]
    return nomes
