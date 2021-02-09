import re
from TimeAllocationModel import *

data = []
dict_semestre = {}
array_semestre = []
dict_disciplina = {}

print("Alocação de Horários")


entrada = """s1
Circuitos Digitais, Carlos
Fundamentos de Programação, Daniel
s2
Laboratório de Programação, Samuel
s3
POO, Marcio
Programação Linear, Ana
s4
Lógica para Computação, João
Comunicação de Dados, José
Estruturas de Dados, Tomás
"""

entrada = entrada.split('\n')

for i in range(len(entrada) - 1):
    entrada_semestre = re.search("^[sS][0-9]{0,2}$", entrada[i])
    if entrada_semestre is not None:
        semestre = entrada_semestre.string
        dict_semestre = {semestre: None}

    entrada_disciplina = re.findall("[a-zA-Z-áàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ\s]+", entrada[i])
    if entrada_disciplina is not None and len(entrada_disciplina) == 2:
        if entrada_disciplina is not None and entrada_disciplina != 's':
            dict_disciplina = {"professor": entrada_disciplina[1].strip(" "), "disciplina": entrada_disciplina[0]}
            array_semestre.append(dict_disciplina)

    if i < len(entrada):
        nova_entrada = re.search("^[sS][0-9]{0,2}$", entrada[i + 1])

        if nova_entrada is not None and nova_entrada != semestre or entrada[i + 1] == '':
            dict_semestre = {semestre: array_semestre}
            data.append(dict_semestre)
            array_semestre = []


solution = time_allocation_solution(data)
for atom in solution:
    if solution[atom]:
        print(atom + ": " + str(solution[atom]))


