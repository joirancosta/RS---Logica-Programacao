
estudantes = {
    1: {
        'nome': 'Joana',
        'idade': 45,
        'curso': 'Computação'
    },
    2: {
        'nome': 'Ivan',
        'idade': 70,
        'curso': 'Matemática'
    },
    3: {
        'nome': 'Jaqueline',
        'idade': 12,
        'curso': 'Computação'
    }
}

cursos = { 'Computação', 'Matemática', 'Física' }

estudantes_cusos = {
    'Computação': { 1, 3 },
    'Matemática': { 2 }
}

def adicionar_estudante(matricula, nome, idade, curso):
    pessoa = {
        'nome': nome,
        'idade': idade,
        'curso': curso
    }
    estudantes[matricula] = pessoa
    if curso not in estudantes_cusos:
        estudantes_cusos[curso] = set()
    estudantes_cusos[curso].add(matricula)