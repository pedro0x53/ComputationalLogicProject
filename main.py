import time
from TimeAllocation import *
from SATModerno import *
from SATModerno_fromFormula import *
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

    print('PySAT')
    sat = SATModerno_fromFile()
    sat_start_time = time.time()
    sat.runPySAT_fromFile('CNF Files/Satisfactory/uf50-01.cnf')
    print("Time:", time.time() - sat_start_time)

    # Acho que está dando false porque a formula não está do mesmo formato dos arquivos
    print('PySAT')
    sat2 = SATModerno_fromFormula()
    sat2_start_time = time.time()
    sat2.runPySAT_fromFormula(formula)
    print("Time:", time.time() - sat2_start_time)

    print('\nDPLL')
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

