# Guia de contribuição

Este arquivo reúne alguns combinados para manter o MetaEstudo organizado.

## Antes de alterar

- Leia o arquivo que será alterado e os templates ou scripts que dependem dele.
- Procure por usos da classe, id, variável ou função antes de renomear ou remover algo.
- Confira se já existem alterações locais. Não apague nem reverta trabalho de outra pessoa sem informa-la previamente.
- Faça uma mudança por vez quando possível. Assim fica mais fácil revisar e descobrir a origem de um problema.

## Comentários no código

Comentários devem explicar uma decisão ou o funcionamento de uma parte que não seja óbvia. Eles não precisam repetir o que a linha já deixa claro.


Exemplo de comentario no django:

```django
{# O formulário é inserido aqui por login.html e cadastro.html. #}
{% block auth_content %}
{% endblock %}
```

Mantenha os comentários curtos e próximos do trecho que explicam. Se o código mudar, atualize ou remova o comentário para ele não ficar enganoso.

## CSS e variáveis

- Use as variáveis de `static/css/global/colors.css` para cores.
- Use as variáveis de `static/css/global/typography.css` para família, tamanho, peso e altura de linha.
- Use `static/css/global/variables.css` para raios e espaçamentos compartilhados.
- Não repita valores de cor, fonte ou espaçamento sem necessidade.
- `reset.css` deve conter apenas regras gerais do navegador..
- Os estilos específicos de uma página devem ficar no CSS da própria página, como `home.css` ou `index.css`.

## Templates Django

- Use `{% load static %}` quando o template acessar arquivos estáticos.
- Mantenha a ordem dos estilos: reset, cores, tipografia, variáveis, layout compartilhado e estilo específico da página.
- Não remova um bloco ou include sem verificar as páginas que dependem dele.
- Ao alterar uma classe do template, procure a definição correspondente no CSS e os usos no JavaScript.

## JavaScript

- Use os arquivos globais para comportamentos compartilhados, como tema e navegação.
- Evite duplicar a lógica de tema, menu ou validação em páginas diferentes.

## Fluxo de alteração

1. Faça uma busca curta para entender o trecho que será alterado..
2. Edite somente os arquivos necessários.
3. Teste visualmente as páginas afetadas.
4. Atualize comentários e documentação quando o comportamento mudar.
