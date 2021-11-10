# criptografia

programas para criptografar textos digitados pelo usuário

## Cifra de César

A *Cifra de César* é uma criptografia extremamente simples que consiste em trocar as letras da mensagem em um número fixo de vezes em relação as letras do alfabeto.
Como por exemplo a mensagem "ABC" codificada com a chave "1" ficaria: "BCD".

### chr() e ord()

Para simular algo semelhante ao que a Cifra de César faz foram utilizados as funções `chr()` e `ord()`, a função *ord* converte uma *string* em um número *inteiro* que representa essa string e a função *chr* converte um número *inteiro* em uma *string*, possibilitando uma troca fácil entre as letras das mensagens.

## Cifra de Vigenère

A *Cifra de Vigenère* é um modelo de criptografia que utiliza várias *Cifras de César*, esse modelo possibilita uma criptografia mais complexa que ao invés de utilizar um número para fazer a criptografia, é possível utilizar uma palavra chave para codificar a mensagem.
