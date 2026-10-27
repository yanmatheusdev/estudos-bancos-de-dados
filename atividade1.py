import psycopg2
# Conexão
conexao = psycopg2.connect(
    host="172.16.80.50",
    port="5432",
    database="equipe05",
    user="equipe05",
    password="******"
)
cursor = conexao.cursor()
# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS modalidade (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    alunos INTEGER,
    data_inicio DATE,
    ativa BOOLEAN
)
""")
# INSERT
cursor.execute("""
INSERT INTO modalidade (nome, alunos, data_inicio, ativa)
VALUES
('Musculacao', 30, '2026-01-10', TRUE),
('Pilates', 15, '2026-02-01', TRUE),
('Funcional', 20, '2026-03-05', TRUE),
('Natacao', 25, '2026-04-01', FALSE),
('Crossfit', 18, '2026-05-10', TRUE)
""")
# SELECT *
print("\nTODAS AS MODALIDADES:")
cursor.execute("SELECT * FROM modalidade ORDER BY nome, id")
for linha in cursor.fetchall():
    print(linha)
# SELECT COM WHERE
print("\nMODALIDADES COM MAIS DE 20 ALUNOS:")
cursor.execute("""
SELECT * FROM modalidade
WHERE alunos > 20
ORDER BY nome, id
""")
for linha in cursor.fetchall():
    print(linha)
# SELECT COM ORDER BY
print("\nMODALIDADES ORDENADAS PELO NOME:")
cursor.execute("""
SELECT * FROM modalidade
ORDER BY nome, id
""")
for linha in cursor.fetchall():
    print(linha)
# UPDATE
cursor.execute("""
UPDATE modalidade
SET alunos = 35
WHERE nome = 'Musculacao'
""")
print("\nUPDATE REALIZADO")
# DELETE
cursor.execute("""
DELETE FROM modalidade
WHERE nome = 'Crossfit'
""")
print("DELETE REALIZADO")
conexao.commit()
cursor.close()
conexao.close()
print("\nConexao encerrada.")