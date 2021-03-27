from Formulas import *
from Evaluator import *


evaluator = Evaluator()


def andAll(list_formulas):
    if len(list_formulas) == 1:
        return list_formulas[0]
    elif len(list_formulas) == 2:
        return And(list_formulas[0], list_formulas[1])
    elif len(list_formulas)  > 2:
        return AndAll(*list_formulas)
    else:
        return None


def orAll(list_formulas):
    if len(list_formulas) == 1:
        return list_formulas[0]
    elif len(list_formulas) > 1:
        first_formula = list_formulas[0]
        del list_formulas[0]
        for formula in list_formulas:
            first_formula = Or(first_formula, formula)
        return first_formula
    else:
        return None


# Disciplinas do mesmo porfessor não podem ocorrer no mesmo horário
def professorConstraint(aulas):
    formulas_restricao1 = []
    for semestreAtual in aulas:
        for profAtual in semestreAtual[str(list(semestreAtual.keys())[0])]:
            for horario in range(1, 11):
                for semestre in aulas:
                    for professor in semestre[str(list(semestre.keys())[0])]:
                        if profAtual["professor"] == professor["professor"]:
                            if profAtual["disciplina"] == professor["disciplina"]:
                                continue

                            restricao = Not(And(Atom(
                                str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + profAtual[
                                    "professor"] + "_" + profAtual["disciplina"]),
                                Atom(str(list(semestre.keys())[0]) + "_" + str(horario) + "_" +
                                     professor["professor"] + "_" + professor["disciplina"])))
                            restricao_inv = Not(And(Atom(
                                str(list(semestre.keys())[0]) + "_" + str(horario) + "_" + professor[
                                    "professor"] + "_" + professor["disciplina"]),
                                Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" +
                                     profAtual["professor"] + "_" + profAtual["disciplina"])))

                            if formulas_restricao1.__contains__(restricao_inv):
                                continue
                            else:
                                formulas_restricao1.append(restricao)

    return andAll(formulas_restricao1)


# Disciplinas do mesmo semestre não podem ocorrer no mesmo horário
def semesterConstraints(aulas):
    formulas_restricao2 = []
    for horario in range(1, 11):
        for semestreAtual in aulas:
            for profAtual in semestreAtual[str(list(semestreAtual.keys())[0])]:
                for prof in semestreAtual[str(list(semestreAtual.keys())[0])]:
                    if profAtual == prof:
                        continue

                    restricao = Not(And(Atom(
                        str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + profAtual["professor"] + "_" +
                        profAtual["disciplina"]),
                        Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + prof[
                            "professor"] + "_" + prof["disciplina"])))

                    restricao_inv = Not(And(Atom(
                        str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + prof["professor"] + "_" + prof[
                            "disciplina"]),
                        Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" +
                             profAtual["professor"] + "_" + profAtual["disciplina"])))

                    if formulas_restricao2.__contains__(restricao_inv):
                        continue
                    else:
                        formulas_restricao2.append(restricao)

    return andAll(formulas_restricao2)


# Aulas alocadas em somente um horário
def scheduleConstraints(aulas):
    formulas_restricao3 = []
    formulas_or = []
    for semestreAtual in aulas:
        for profAtual in semestreAtual[str(list(semestreAtual.keys())[0])]:
            for horarioAtual in range(1, 11):
                for horario in range(horarioAtual + 1, 11):
                    if horarioAtual == horario:
                        continue

                    atom0 = Atom(str(list(semestreAtual.keys())[0]) + "_1_" + profAtual["professor"] + "_" + profAtual[
                        "disciplina"])
                    atom1 = Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horarioAtual) + "_" + profAtual[
                        "professor"] + "_" + profAtual["disciplina"])
                    atom2 = Atom(
                        str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + profAtual["professor"] + "_" +
                        profAtual["disciplina"])

                    formulas_restricao3.append(Not(And(atom1, atom2)))

                    if not formulas_or.__contains__(atom1):
                        formulas_or.append(atom1)
                    if not formulas_or.__contains__(atom2):
                        formulas_or.append(atom2)
                    if not formulas_or.__contains__(atom0):
                        formulas_or.clear()
                    if len(formulas_or) == 10 and horarioAtual == 1 and horario == 10:
                        restricao3_or = orAll(formulas_or)
                        formulas_restricao3.insert(0, restricao3_or)
                        formulas_or.clear()

    return andAll(formulas_restricao3)


def time_allocation_solution(aulas):
    restricoesProfessor = professorConstraint(aulas)
    restricoessemestre = semesterConstraints(aulas)
    restricoesHorario = scheduleConstraints(aulas)

    finalFormula = None

    if restricoesProfessor != None:
        if restricoessemestre != None:
            if restricoesHorario != None:
                finalFormula = And(
                    And(restricoesProfessor, restricoessemestre),
                    restricoesHorario
                )
            else:
                finalFormula = And(restricoesProfessor, restricoessemestre)
        else:
            finalFormula = restricoesProfessor
    elif restricoessemestre != None:
        if restricoesHorario != None:
            finalFormula = And(restricoesHorario, restricoessemestre)
        else:
            finalFormula = restricoessemestre
    elif restricoesHorario != None:
        finalFormula = restricoesHorario
    else:
        print("Nenhuma solução foi encontrada.")
        return 0

    # return evaluator.satisfability(finalFormula, mode=Evaluator.satisfactory)
    return finalFormula
