-- CREATE TABLE
CREATE TABLE IF NOT EXISTS modalidade (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    alunos INTEGER,
    data_inicio DATE,
    ativa BOOLEAN
);

-- INSERT
INSERT INTO modalidade (nome, alunos, data_inicio, ativa)
VALUES
('Musculacao', 30, '2026-01-10', TRUE),
('Pilates', 15, '2026-02-01', TRUE),
('Funcional', 20, '2026-03-05', TRUE),
('Natacao', 25, '2026-04-01', FALSE),
('Crossfit', 18, '2026-05-10', TRUE);

-- SELECT * (todas as modalidades)
SELECT * FROM modalidade ORDER BY id;


-- SELECT com WHERE (mais de 20 alunos)
SELECT * FROM modalidade

DELETE FROM modalidade WHERE id = 4;

-- SELECT com ORDER BY (ordenadas pelo nome)
SELECT * FROM modalidade
ORDER BY nome;

-- UPDATE
UPDATE modalidade
SET alunos = 35
WHERE nome = 'Musculacao';

-- DELETE
DELETE FROM modalidade
WHERE nome = 'Crossfit';
