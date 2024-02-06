# Pos Helper

> Projeto final para o curso Introdução à Ciencia da Computação (CS50), oferecido pela Universidade de Harvard.

#### Vídeo Demo: https://www.youtube.com/watch?v=V4GneXWV0MY

#### Descrição:

## Visão geral

Uma ferramenta de auxílio para inserir informações em planílhas do Excel.

No meu dia a dia, eu me encontro repetindo constantemente a mesma atividade, que é transferir informação dada pelos clientes da empresa em que trabalho para um relatório no Excel, então desenvolvi essa aplicação para atuar como suporte em meus dias de serviço.

Como trabalho no setor de controle de qualidade, preciso criar relatórios que indicam a perfomance de nossos times. Para isso, mantenho registro de informações relevantes, tais como o nome da equipe, a data da visita técnica, o ID e telefone dos clientes que entro em contato, e por fim, o feedback recebido, bem como a transcrição do contato que fiz e a nota recebida pela equipe.

Todos os algoritmos foram implementados em Python, utilizando a tecnologia Flask para configurar o servidor. Toda a estrutura foi feita com HTML e CSS, com a ajuda ocasional do framework Bootstrap.

O backend do site funciona através da implementação de um banco de dados relacional, onde envio informação para uma tabela e no fim seleciono as informações que quero, tudo feito através de comandos SQL.

## Stack Utilizada
[![My Skills](https://skillicons.dev/icons?i=py,html,css,bootstrap,flask,sqlite,git)](https://skillicons.dev)


## Página inicial

Na página inicial posso inserir as informações citadas acima, todos os dados inseridos são enviados para um banco de dados que os mantém em segurança. Atualmente utilizo sqlite3, porém planejo transferir para MySQL em um futuro próximo.

![Página Inicial](/imgs/image.png)

## Exportar

Na página de exportação, posso copiar a informação inserida anteriormente, já formatada como tabela e em seguida colar em minhas planilhas, assim posso gerar um relatório mais rapidamente, o que gera uma melhor perfomance em minhas tarefas diárias.

![Aba de exportação](/imgs/image-1.png)
![Aba de exportação com conteúdo](/imgs/image-2.png)

## Adicionar novas equipes

Como no mercado trabalhista existe uma alta rotatividade de funcionários, adicionei a opção para adicionar novas equipes, muito fácil de utilizar, apenas insira o nome da equipe e prontinho!

![Adicionar novas equipes](/imgs/image-3.png)

## Excluir informação

Além de todas as funções já citadas, também fiz a implementação de dois botões cuja finalidade é apenas de excluir informação.
O primeiro exclui toda a informação registrada anteriormente, para que possa começar novos relatórios sem dados sobrescritos, o segundo exclui todos os times cadastrados, útil quando precisamos informar equipes de outras filiais.

![Botões de excluir informação](/imgs/image-4.png)

## Planos futuros

Como este projeto irá resolver um problema que eu venho enfrentando por vários meses, irei continuar a implementar funcionalidades e melhorar as características já existentes. Algumas melhorias que já tenho em mente são:

-   Alerta de erro ao tentar enviar informação sem selecionar uma equipe
-   Refazer o frontend
-   Adicionar alerta para confirmar antes de excluir informação através dos botões correspondentes
-   Entre outras

## Como utilizar

Após clonar o repositório e instalar os requerimentos, bastar rodar o comando ```flask run``` para inicializar o servidor local.

## Considerações finais

Estou muito feliz em ter finalizado o curso, acredito que o conhecimento adquirido irá me acompanhar durante toda minha vida! <p>
Todos os meus agradecimentos vão para o excelente professor David J. Malan, dono de uma didática impecável que fez com que assuntos difíceis se tornassem agradáveis de estudar, bem como à todo o time responsável pelo curso. <p>
Foi apenas o primeiro passo na minha jornada como desenvolvedor, mas eu acredito que foi o mais importante. <p>
Mais uma vez, agradeço a todos! <p>

<h2 style="text-align: center;"> This is CS50.
