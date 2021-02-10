import re
from TimeAllocationModel import *

print("Alocação de Horários")

entrada = """s1
p0a, d0a
p1a, d1a
p2a, d2a
p3a, d3a
p4a, d4a
p5a, d5a
p6a, d6a
p7a, d7a
p8a, d8a
p9a, d9a
s2
p0b, d0b
p1b, d1b
p2b, d2b
p3b, d3b
p4b, d4b
p5b, d5b
p6b, d6b
p7b, d7b
p8b, d8b
p9b, d9b
s3
p0c, d0c
p1c, d1c
p2c, d2c
p3c, d3c
p4c, d4c
p5c, d5c
p6c, d6c
p7c, d7c
p8c, d8c
p9c, d9c
s4
p0d, d0d
p1d, d1d
p2d, d2d
p3d, d3d
p4d, d4d
p5d, d5d
p6d, d6d
p7d, d7d
p8d, d8d
p9d, d9d
s5
p0e, d0e
p1e, d1e
p2e, d2e
p3e, d3e
p4e, d4e
p5e, d5e
p6e, d6e
p7e, d7e
p8e, d8e
p9e, d9e
s6
p0f, d0f
p1f, d1f
p2f, d2f
p3f, d3f
p4f, d4f
p5f, d5f
p6f, d6f
p7f, d7f
p8f, d8f
p9f, d9f
s7
p0g, d0g
p1g, d1g
p2g, d2g
p3g, d3g
p4g, d4g
p5g, d5g
p6g, d6g
p7g, d7g
p8g, d8g
p9g, d9g
s8
p0h, d0h
p1h, d1h
p2h, d2h
p3h, d3h
p4h, d4h
p5h, d5h
p6h, d6h
p7h, d7h
p8h, d8h
p9h, d9h
s9
p0i, d0i
p1i, d1i
p2i, d2i
p3i, d3i
p4i, d4i
p5i, d5i
p6i, d6i
p7i, d7i
p8i, d8i
p9i, d9i
s10
p0j, d0j
p1j, d1j
p2j, d2j
p3j, d3j
p4j, d4j
p5j, d5j
p6j, d6j
p7j, d7j
p8j, d8j
p9j, d9j
"""

entrada = entrada.split('\n')


data = []
nomeSemestreAtual = None
professoresDisciplinas = []

for linha in entrada:
    novoSemestreMatch = re.search("^[sS][0-9]{1,2}$", linha)
    if novoSemestreMatch is not None:
        if nomeSemestreAtual is not None and len(professoresDisciplinas) > 0:
            data.append({nomeSemestreAtual: professoresDisciplinas})
            professoresDisciplinas = []
        nomeSemestreAtual = novoSemestreMatch.string
        continue

    professorDisciplinaMatch = re.search("^.+, .+$", linha)
    if professorDisciplinaMatch is not None:
        professorDisciplina = professorDisciplinaMatch.string.split(", ")
        professoresDisciplinas.append({"professor": professorDisciplina[0], "disciplina": professorDisciplina[1]})


data.append({nomeSemestreAtual: professoresDisciplinas})
nomeSemestreAtual = None
professoresDisciplinas = []

# Solução
print(time_allocation_solution(data))