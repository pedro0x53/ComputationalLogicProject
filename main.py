import time
from TimeAllocation import *
from SATModerno import *
from SATModerno_fromFormula import *
from DPLL import *
from Evaluator import *
from Tableaux import *


def runPySAT():
    print('Arquivos CNF - PySAT')

    sat = SATModerno_fromFile()

    print('\nSatisfatório')

    print('1º Arquivo')
    print(sat.runPySAT_fromFile('CNF Files/Satisfactory/uf50-01.cnf'))

    print('2º Arquivo')
    print(sat.runPySAT_fromFile('CNF Files/Satisfactory/uf50-02.cnf'))

    print('3º Arquivo')
    print(sat.runPySAT_fromFile('CNF Files/Satisfactory/uf50-03.cnf'))

    print('\nInstisfatório')
    print('1º Arquivo')
    print(sat.runPySAT_fromFile('CNF Files/Unsatisfactory/uuf50-01.cnf'))

    print('2º Arquivo')
    print(sat.runPySAT_fromFile('CNF Files/Unsatisfactory/uuf50-02.cnf'))

    print('3º Arquivo')
    print(sat.runPySAT_fromFile('CNF Files/Unsatisfactory/uuf50-03.cnf'))


def runDPLL():
    print('\nArquivos CNF - DPLL')

    dpll = DPLL()
    print('\nSatisfatório')

    print('1º Arquivo')
    print(sorted(dpll.runFromFile('CNF Files/Satisfactory/uf50-01.cnf'), ))

    print('2º Arquivo')
    print(dpll.runFromFile('CNF Files/Satisfactory/uf50-02.cnf'))

    print('3º Arquivo')
    print(dpll.runFromFile('CNF Files/Satisfactory/uf50-03.cnf'))

    print('\nInstisfatório')
    print('1º Arquivo')
    print(dpll.runFromFile('CNF Files/Unsatisfactory/uuf50-01.cnf'))

    print('2º Arquivo')
    print(dpll.runFromFile('CNF Files/Unsatisfactory/uuf50-02.cnf'))

    print('3º Arquivo')
    print(dpll.runFromFile('CNF Files/Unsatisfactory/uuf50-03.cnf'))


def timeComparison():
    print('\n\nTime Comparison\n')
    formula = getFormula()

    print('PySAT')
    sat = SATModerno_fromFile()
    sat_start_time = time.time()
    sat.runPySAT_fromFile('CNF Files/Satisfactory/uf50-01.cnf')
    print("Time:", time.time() - sat_start_time)

    print('\nPySAT from formula')
    sat2 = SATModerno_fromFormula()
    sat2_start_time = time.time()
    sat2.runPySAT_fromFormula(formula)
    print("Time:", time.time() - sat2_start_time)

    print('\nDPLL')
    dpll = DPLL()
    dpll_start_time = time.time()
    dpll.runFromFormula(formula)
    print("Time:", time.time() - dpll_start_time)

    print('\nTableaux')
    valuesFormulas4 = [1]
    tableaux_start_time = time.time()
    print(satisfiability_tableaux(tableaux_start_time, [formula], valuesFormulas4, max_time=10))
    print('Time:', time.time() - tableaux_start_time)

    print('\nEvaluator')
    evaluator = Evaluator()
    evaluator_start_time = time.time()
    evaluator.satisfiability(formula, mode=Evaluator.satisfactory)
    print("Time:", time.time() - evaluator_start_time)



if __name__ == "__main__":
    runPySAT()
    runDPLL()
    timeComparison()

