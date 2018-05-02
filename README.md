# Introdução ao Hadoop

Este projeto faz parte dos projetos disponiveis no nanodegree de Fundamentos de Data Science II da Udacity

Será Utilizado Hadoop com Mapeadores e Redutores e fazendo processamento de dados em um cluster local pseudo-distribuído.

São dois experimentos em duas bases de dados diferentes, a primeira com um conjunto de dados de vendas para a seguinte finalidade:
1.1 - Encontrar as vendas por categoria de produto em todas as nossas lojas.
1.2 - Encontrar o valor monetário para a maior venda individual para cada loja separadamente.
1.3 - Encontrar o valor total das vendas em todas as lojas e o número total de vendas. 

O segundo conjunto de dados que usado é um arquivo de log do servidor web anonimizado de uma empresa de relações públicas cujos clientes eram distribuidores de DVD.

O arquivo de log está em Common Log Format:
Aqui os mapeadores e redutores são utilizados para:
2.1 - Quantos acessos foram realizados a uma página especifica
2.2 - Quantos acessos foram feitos por um dado ip
2.3 - Qual página mais popular e qual o número de acessos da mesma

Para criação e execução dos testes foi utilizada a VM oficial do Hadoop
Para rodar os exercicios utiliza-se o comando:
cat data | python mapper.py | sort | python reducer.py