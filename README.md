# Web scraping *gupy*
## Sobre
Esse é um projeto de extração e análise de dados de vagas de emprego na plataforma [Gupy](https://portal.gupy.io), com Python.                                                                                              
Tecnologias utilizadas: `Python, BeautifulSoup, selenium, pandas, matplotlib, numpy, time, requests`.

Como o objetivo é extrair o máximo de dados de vagas possível, tentei encontrar as palavras chaves que mais obtessem resultados. 
O termo `estágio` obteve um número considerável de respostas, com mais de 2500 vagas.

## Metodologia
Esse código consite em utilizar `selenium` para abrir a plataforma Gupy em um driver Chrome, pesquisar "estágio", *scrollar* até a última vaga 
disponível, salvar o conteúdo do *html* com `BeautifulSoup` e exportar dados tabulares com `pandas`. 

-> **[/main/main.py](https://github.com/marcoaguibor/web-scraping-gupy/blob/main/main/main.py):** apresenta essa metodologia, desde a importação dos  módulos utilizados, extrair e salvar os dados em uma lista de listas e transformá-los em um dataframe .csv;   
-> **[/data/data.csv](https://github.com/marcoaguibor/web-scraping-gupy/blob/main/data/data.csv):** são os dados já salvos, com 11 colunas (variáveis) e mais de 2500 linhas (vagas abertas);     
-> **[/plot](https://github.com/marcoaguibor/web-scraping-gupy/tree/main/plot):** contém os arquivos .jpeg dos gráficos criados;

-> **[data_analysis.ipynib](https://github.com/marcoaguibor/web-scraping-gupy/blob/main/data_analysis.ipynb):** apresenta os resultados, com os códigos para os gráficos e interpretações.

## Resultados
-Dividindo os dados por unidade federativa, obtemos alguns resultados: São Paulo possui o maior número de vagas, seguido por Minas Gerais, Rio Grande do Sul e Paraná. Alguns estados encontram-se com pouquíssimas vagas disponíveis, como Amapá e Piauí.
<p align="left">
  <img src="plots/n_vagas_por_uf.jpeg" alt="Número de vagas por UF">
</p>
