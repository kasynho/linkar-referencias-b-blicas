import re

biblia = {'Gn': '1', 'Ex': '2'}
texto = "Gn 10:15-19; 12:7; 15:7,18-21; 19:10-14,16;20:3—21:7; Ex 2:5;"
pattern = re.compile(r'\b((?:[123]\s?)?(?:I*\s?)?[A-ZÀ-Ü][a-zà-ü]+\.?)(\s\d+:)?([\d,-;—\s–:]+\d+)\b')


def linkar_versos(match):
    livro = biblia[match.group(1)]
    capitulo_versiculo = match.group(3)  # 15-19; 12:7; 15:7,18-21; 19:10-14,16;20:3—21:7
    referencias = re.split(r'[;,]', capitulo_versiculo)
    links = []
    for ref in referencias:
        if '-' in ref:
            inicio, fim = ref.split('-')
            links.append(f'{livro}.{ref[0]}.{inicio}-{livro}.{ref[0]}.{fim}')
        elif '—' in ref:
            cap_inicio, vers_inicio, cap_fim, vers_fim = ref.split('—')
            links.append(f'{livro}.{cap_inicio}.{vers_inicio}-{livro}.{cap_fim}.{vers_fim}')
        else:
            links.append(f'{livro}.{ref}')
    return ', '.join([f"<a href='b{link}'>{match.group(1)} {ref}</a>" for ref, link in zip(referencias, links)])


result = re.sub(pattern, linkar_versos, texto)
print(result)
