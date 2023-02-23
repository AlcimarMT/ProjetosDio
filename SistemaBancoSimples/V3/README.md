# O sistema V3

O sistema V3 emprega a programação orientada ao objeto para executar as mesmas funções dos códigos anteriores.

No primeiro contexto que é impresso no terminal, a pessoa pode escolher entre informar o nome de um cliente e entrar no contexto do administrador pelo uso do nome 'adm'.

A alimentação do nome de um cliente foi escolhida como parâmetro para o registro dos objetos de clientes para facilitar os testes do código. Caso o registro fosse feito por códigos ou emails, a lentidão em iterar através dos diferentes contextos ou âmbitos aumentaria.

Num primeiro momento, o contexto 'normal' reqer o nome de um cliente. O programa, então, procura por esse cliente na lista de contas bancárias, e posteriormente na lista de usuários cadastrados. Caso o cliente esteja em ambas as listas, será possível realizar as operações de depósito, saque, extrato, e obtenção de dados da conta.

A alimentação de qualquer informação que não seja um número real nos âmbitos do deposito e do saque resultará em erro.

Há também outros dois âmbits - extrato e dados.

O Extrato fornece uma lista com todas as operações de deposito e de saque realizadas na conta do cliente

O dados é um âmbito onde há o retorno das informações de nome, tipo, senha e saldo do cliente.

No contexto de adm é possível realizar as operações de registro de novos clientes nas listas de usuários e de contas bancárias. Imprimir essas listas também é possível com os comandos relativos a cada lista.

