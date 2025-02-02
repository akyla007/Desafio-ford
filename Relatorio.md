# Relatório do Projeto - Desafio Ford

## Introdução
Este relatório apresenta as atividades desenvolvidas no projeto Desafio Ford, onde atuei como cientista de dados. O objetivo foi analisar dados de reclamações de veículos dos anos de 2023 a 2025, utilizando 2025 para testar o modelo treinado com dados de 2023 e 2024.

Alguns trechos do código ainda necessitam de refatoração para remover bad smells e melhorar a modularização.

Para instalar as dependências, siga as instruções no Readme.md.

## Coleta de Dados
A primeira etapa do projeto envolveu a coleta de dados de diversas fontes, incluindo:
- Automatização da coleta de dados via API, seguindo a sequência: fabricantes, modelos produzidos nos anos estudados e reclamações de cada veículo e fabricante com base no ano de estudo.
- Otimização do código para melhorar as chamadas à API, evitando complexidade O(m*n*k).

## Limpeza e Preparação dos Dados
Após a coleta, os dados foram limpos e preparados para análise, incluindo:
- Remoção de valores nulos
- Tratamento de outliers
- Transformação de dados

## Conclusão
O projeto envolve vários pontos a serem analisados para extrair insights interessantes. Devido ao tempo limitado, não consegui implementar todas as ideias, mas resumo abaixo as intenções e abordagens planejadas.

## Próximos Passos
Para futuras iterações do projeto, recomendo:
- Analisar outliers e valores indesejados nos dados extraídos da API, convertidos para formatos mais manejáveis.
- Organizar os dados na estrutura de pastas em `src/data`, contendo arquivos bronze, silver e gold, seguindo a arquitetura de medalhão.
- Tratar a coluna de reclamações usando processamento de linguagem natural (PLN) com ferramentas do NLTK para extrair as palavras mais frequentes nas reclamações de cada modelo e criar uma coluna com essas palavras (centro da reclamação).
- Após a modelagem e extração com PLN, extrair insights baseados na nova coluna, identificando as peças/problemas mais recorrentes de cada modelo de carro.

## Agradecimentos
Agradeço a Vitor Hugo Duarte pela oportunidade de participar desse desafio.

## Contato
Para mais informações, entre em contato:
- Nome: Akyla Aquino
- Email: akylaaquino@hotmail.com
- LinkedIn: [Akyla Aquino](https://www.linkedin.com/in/akyla-aquino/)
