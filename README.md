
Preciso de um Script no python para linkar versos de texto bíblico.
Veja para encontrar as referências nesta string texto = "Gn 10:15-19; 12:7; 15:7,18-21; 19:10-14,16;20:3—21:7; Ex 2:5;"
Uso a regex "re.findall(r'\b((?:[123]\s?)?(?:I*\s?)?[A-ZÀ-Ü][a-zà-ü]+\.?)(\s\d+:)?([\d,-;—\s–:]+\d+)\b', texto)"

O findall retorna dois grupos, o primeiro grupo é abreviação do livro, segundo gruipo são as referências;

A linkagem é feita desta funciona desta maneira:
<a href='b{livro}.{capitulo}.{versiculo}'>Gn 12:7</a>

também pode ter casos assim:
<a href='b{livro}.{capitulo}.{versiculo_inicio}-{livro}.{capitulo}.{versiculo_fim}'>Gn 12:7-15</a>

para referencias de um capítulo a outro pode ser assim:
<a href='b{livro}.{capitulo}.{inicio}-{livro}.{capitulo}.{fim}'>Gn 20:3—21:7</a>

Dicionário para converter os livros da bíblia para números:
biblia = {'Gn': '1', 'Ex': '2'}

o segundo grupo da regex preciso separar desta maneira:
; separa referencia 
: Separa capitulo
, separa versiculo
- separa versículo início e versículo fim
— indica capítulo+inicio a capítulo+fim

as referências podem ser apresentadas assim:
10:15-19 = capítulo+versiculo inicio+versículo fim
12:7= capítulo + versículo
15:7,18-21 = capítulo+versiculo+versiculo inicio+versículo fim
19:10-14,16= capítulo+versiculo inicio+versículo fim+versiculo
20:3—21:7= — indica capítulo+versículo a capítulo+versiculo
