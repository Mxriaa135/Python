# ANOTAÇÕES CAPÍTULO 2
## VARIÁVEIS
### O que são? 
Variáveis são espaços reservados na memória do computador com o objetivo de armazenar, temporariamente, um determinado dado
### Tipos de dados
#### Tipo numérico
- Numeros flutuantes: São os números que podem fazer uso das casas decimais, como altura, preço, peso, etc. O tipo double tem o dobro de precisão nas casas decimais que o tipo float, por isso ocupa um espaço maior na memória. 
- Numeros inteiros: Números que não necessitam de casas decimais, como: idade, data, quantidade de objetos, etc. Utilizamos o tipo int.
#### Tipo Alfanumérico
- É o dado que jamais será usado para fazer contas matemáticas, como nome, cpf, rg, etc. Utilizamos o tipo string, que representa um conjunto de caracteres. Outras linguagens se utilizam do char, que representa apenas um caractere.

### Observações
- o "Input()" tem como finalidade armazenar um dado que é passado pelo usuário, em uma variável.
- Quando uma variável do tipo numérico é exibida em um texto e concatenada através do operador "+", é necessário utilizar a função "str()" para que o Python não realize uma operação matemática.
- A função "type()" tem como finalidade informar o tipo do dado armazenado na variável.

## TOMADAS DE DECISÕES (if)
### O que São?
Uma tomada de decisão em um código refere-se ao ponto em que o programa precisa escolher entre diferentes caminhos de execução, com base em uma condição ou conjunto de condições. Utiliza-se os comandos condicionais "if", "else" e "elif".

#### Decisões simples
- São formadas para avaliar apenas uma hipótese. Utiliza-se apenas o "if".
#### Decisões compostas
- São formadas para avaliar duas hipóteses. Utiliza-se o "if" e o "else".
#### Decisões encadeadas
- São formadas para avaliar três hipóteses. Utiliza-se o "if", o "else" e o "elif".

### Observações
- As linhas a serem executadas, abaixo do if, caso a condição for verdadeira, devem estar com um recuo da margem esquerda, através do "Tab".
- A função "upper()" tem como finalidade converter o conteúdo de uma string, inserido pelo usuário, para letras maiúsculas.