from pysat.solvers import Glucose3
from CNF import *


class SATModerno_fromFormula:
    def __init__(self):
        self.cnf = CNF()

    def runPySAT_fromFormula(self, formula):
        list_clauses = []
        relationAndClauses = self.cnf.formulaToCNFClauses(formula)
        clauses = list(relationAndClauses.get("clauses"))
        glucose = Glucose3()

        for clause in clauses:
            list_clauses.append(list(clause))

        glucose.append_formula(list_clauses)
        return glucose.solve()
