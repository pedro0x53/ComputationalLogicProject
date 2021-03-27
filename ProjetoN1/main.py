import re
from TimeAllocationModel import *
from DPLL import *

# print("Alocação de Horários")

entrada = """s1
p0a, d0a
p1a, d1a
s2
p0b, d0b
p1b, d1b
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

 
if __name__ == "__main__":
    formula = time_allocation_solution(data)
    dpll = DPLL()
    print(dpll.runFromFormula(formula))
    print(dpll.runFromFile("CNF Files/Satisfactory/uf50-01.cnf"))
