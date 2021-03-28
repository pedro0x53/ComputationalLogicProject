from pysat.solvers import Glucose3
from CNF import *


class SATModerno_fromFormula:
    def __init__(self):
        self.cnf = CNF()

    def runPySAT_fromFormula(self, formula):
        relationAndClauses = self.cnf.formulaToCNFClauses(formula)
        clauses = list(relationAndClauses.get("clauses"))

        glucose = Glucose3()
        glucose.append_formula(clauses)
        print(glucose.solve())
