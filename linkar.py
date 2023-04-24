# Preciso de um Script no python para linkar versos de texto bíblico.
# Veja para encontrar as referências nesta string 
# texto = "Gn 10:15-19; 12:7; 15:7,18-21; 19:10-14,16;20:3—21:7; Ex 2:5;"

# Uso a regex
#referencias = "re.findall(r'\b((?:[123]\s?)?(?:I*\s?)?[A-ZÀ-Ü][a-zà-ü]+\.?)(\s\d+:)?([\d,-;—\s–:]+\d+)\b', texto)"
 
# O findall retorna dois grupos, o primeiro grupo é abreviação do livro, segundo grupo são as referências;
 
# A linkagem é feita desta funciona desta maneira:
# Para Gn 12:7
# <a href='b{livro}.{capitulo}.{versiculo}'>Gn 12:7</a>
# <a href='b1.12.7'>Gn 12:7</a>

# Para Gn 12:7-15
# <a href='b{livro}.{capitulo}.{verso_inicio}-{livro}.{capitulo}.{verso_fim}'>Gn 12:7-15</a>
# <a href='b1.12.7-1.12.15'>Gn 12:7-15</a>

# Para Gn 2:8-10,18 
# <a href='b{livro}.{capitulo}.{verso_inicio}-{livro}.{capitulo}.{verso_fim}'>Gn 2:8-10</a>, <a href='b{livro}.{capitulo}.{versiculo}'>18</a>
# <a href='b1.2.8-1.2.10'>Gn 2:8-10</a>,<a href='b1.2.18'>18</a>

# Para Gn 20:3—21:7
# <a href='b{livro}.{capitulo}.{verso-inicio}-{livro}.{capitulo}.{verso_fim}'>Gn 20:3—21:7</a>
# <a href='b1.20.3-1.21.7'>Gn 12:7-15</a>
 
# Preciso de um dicionário para converter os livros da bíblia para números:
# biblia = {'Gn': '1', 'Ex': '2'}
 
# o segundo grupo da regex preciso separar desta maneira:
# ; separa referencia 
# : Separa capitulo
# , separa versiculo
# - separa versículo início e versículo fim
# — indica capítulo+inicio a capítulo+fim

# as referências podem ser apresentadas assim:
# 12:7= capítulo + versículo
# 15:18-21 = capítulo+versiculo+versiculo inicio+versículo fim
# 19:10-14,16= capítulo+versiculo inicio+versículo fim+versiculo|capítulo+versiculo
# 20:3—21:7= — indica capítulo+versículo a capítulo+versiculo


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
