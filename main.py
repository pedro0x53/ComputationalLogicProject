import time
from TimeAllocation import *
# from SATModerno import *
from DPLL import *
from Evaluator import *


def runDPLL():
    print('Arquivos DPLL')

    dpll = DPLL()
    print('\nSatisfatório')

    print('1º Arquivo')
    print(dpll.runFromFile('CNF Files/Satisfactory/uf50-01.cnf'))

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

    print('DPLL')
    dpll = DPLL()
    dpll_start_time = time.time()
    dpll.runFromFormula(formula)
    print("Time:", time.time() - dpll_start_time)

    print('\nEvaluator')
    evaluator = Evaluator()
    evaluator_start_time = time.time()
    evaluator.satisfiability(formula, mode=Evaluator.satisfactory)
    print("Time:", time.time() - evaluator_start_time)



if __name__ == "__main__":
    runDPLL()
    timeComparison()

