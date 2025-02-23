import sqlite3

conexao = sqlite3.connect(r'C:\Users\marin\OneDrive\Área de Trabalho\BOOTCAMP WOMAKERSCODE\BANCO_DE_DADOS\EX_BANCO_DE_DADOS.db')
cursor = conexao.cursor()

# EX. 1
# Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
# cursor.execute('CREATE TABLE IF NOT EXISTS alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')



# EX. 2
# Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "MARINA", 28, "Engenharia Física")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "MARIA", 27, "Engenharia de Produção")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "JOÃO", 26, "Administração")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "JOSÉ", 25, "Arquitetura")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "LETÍCIA", 29, "Direito")')



# EX. 3 a) Selecionar todos os registros da tabela "alunos".
# dados = cursor.execute('SELECT * FROM alunos')
# for variavel_for in dados:
#     print(variavel_for)


# EX. 3 b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
# dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
# for variavel_for in dados:
#     print(variavel_for)


# cursor.execute('UPDATE alunos SET idade = 18 where id = 4')

# dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
# dados = cursor.execute('SELECT * FROM alunos')
# for variavel_for in dados:
#     print(variavel_for)


# EX. 3 c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
# dados = cursor.execute('SELECT * FROM alunos WHERE curso like "%Engenharia%" ORDER BY nome')
# for variavel_for in dados:
#     print(variavel_for)


#  EX. 3 d) Contar o número total de alunos na tabela
# dados = cursor.execute('SELECT count(nome) as qtde_alunos FROM alunos')
# for variavel_for in dados:
#     print(variavel_for)



# EX. 4 a) Atualize a idade de um aluno específico na tabela.
# cursor.execute('UPDATE alunos SET idade = 36 where id = 3')

# dados = cursor.execute('SELECT * FROM alunos')
# for variavel_for in dados:
#     print(variavel_for)


# EX. 4 b) Remova um aluno pelo seu ID.

# cursor.execute('DELETE FROM alunos WHERE id = 5')

# dados = cursor.execute('SELECT * FROM alunos')
# for variavel_for in dados:
#     print(variavel_for)



# EX. 5 
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float).
# cursor.execute('CREATE TABLE clientes(id INTEGER primary key AUTOINCREMENT, nome VARCHAR(100), idade INT, saldo FLOAT)')


# Insira alguns registros de clientes na tabela.
# cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("MARINA", 28, 8910.45)')
# cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("MARIA", 27, 4567.45)')
# cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("JOÃO", 36, 1234.45)')
# cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("JOSÉ", 18, 1112.45)')
# cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("LETÍCIA", 29, 1314.45)')


# dados = cursor.execute('SELECT * FROM clientes')
# for variavel_for in dados:
#     print(variavel_for)



# EX. 6 a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
# dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
# for variavel_for in dados:
#     print(variavel_for)


# EX. 6 b) Calcule o saldo médio dos clientes.
# dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
# for variavel_for in dados:
#     print(variavel_for)


# EX. 6 c) Encontre o cliente com o saldo máximo.
# dados = cursor.execute('SELECT * FROM clientes WHERE saldo = (SELECT max(saldo) FROM clientes)')
# for variavel_for in dados:
#     print(variavel_for)


# EX. 6 d) Conte quantos clientes têm saldo acima de 1000.
# dados = cursor.execute('SELECT COUNT(nome) FROM clientes WHERE saldo > 1000')
# for variavel_for in dados:
#     print(variavel_for)


# cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES("SERGIO", 20, 850)')
# cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES("MARCIA", 45, 3000)')

# dados = cursor.execute('SELECT COUNT(nome) FROM clientes WHERE saldo > 1000')
# for variavel_for in dados:
#     print(variavel_for)



# EX. 7 a) Atualize o saldo de um cliente específico.
# cursor.execute('UPDATE clientes SET saldo = 10000.00 WHERE nome = "MARINA"')

# dados = cursor.execute('SELECT * FROM clientes')
# for variavel_for in dados:
#     print(variavel_for)


# EX. 7 b) Remova um cliente pelo seu ID.
# cursor.execute('DELETE FROM clientes WHERE id = 4')

# dados = cursor.execute('SELECT * FROM clientes')
# for variavel_for in dados:
#     print(variavel_for)



# EX. 8 Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id
#  da tabela "clientes"), produto (texto) e valor (real).

# cursor.execute('CREATE TABLE compras(id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id INTEGER, produto VARCHAR(50), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE)')


# EX. 8 Insira algumas compras associadas a clientes existentes na tabela "clientes".
# cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(1, "Notebook", 3500.00)')
# cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(2, "Smartphone", 2200.50)')
# cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(3, "Fones de ouvido", 150.75)')
# cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(1, "Mouse sem fio", 120.00)')
# cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(7, "Monitor 24", 899.99)')


# EX. 8 Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
# dados = cursor.execute('SELECT A.nome, B.produto, B.valor FROM clientes AS A LEFT JOIN compras as B on (A.id = B.cliente_id) ORDER BY 1,3')
# for variavel_for in dados:
#     print(variavel_for)

dados = cursor.execute('SELECT A.nome, B.produto, B.valor FROM compras AS B LEFT JOIN clientes as A on (A.id = B.cliente_id) ORDER BY 1,3')
for variavel_for in dados:
    print(variavel_for)




conexao.commit()
conexao.close