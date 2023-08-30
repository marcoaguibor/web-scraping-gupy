# Web scraping *gupy*
## Sobre
Esse é um projeto de extração e análise de dados de vagas de emprego na plataforma [Gupy](https://portal.gupy.io), com Python.                                                                                              
Tecnologias utilizadas: `Python, BeautifulSoup, selenium, pandas, matplotlib, time, requests`.

Como o objetivo é extrair o máximo de dados de vagas possível, tentei encontrar as palavras chaves que mais obtessem resultados. 
O termo `estágio` foi o que mais teve respostas, com mais de 2500 vagas.

## Metodologia
Esse código consite em utilizar `selenium` para abrir a plataforma Gupy em um driver Chrome, pesquisar "estágio", *scrollar* até a última vaga 
disponível e salvar o conteúdo do html com `BeautifulSoup` e exportar dados tabulares com `pandas`. 

-> **main.py** apresenta essa metodologia, desde a importação dos  módulos utilizados, extrair e salvar os dados em uma lista de listas e transformá-los 
em um dataframe csv;   
-> **data** são os dados já salvos, com 11 colunas (variáveis) e mais de 2500 linhas (vagas abertas);     
-> **plot.py** são os códigos para criação dos gráficos.      

## Resultados

**[EM ANDAMENTO]**
