from Formulas import *

class Formatter:
    def __init__(self):
        pass

    def replace(self, formula, old, new):
        if formula == old:
            return new

        if isinstance(formula, Atom):
            return Atom(formula.name)

        if isinstance(formula, Not):
            return Not(self.replace(formula.inner, old, new))

        if isinstance(formula, And):
            return And(self.replace(formula.left, old, new), self.replace(formula.right, old, new))

        if isinstance(formula, Or):
            return Or(self.replace(formula.left, old, new), self.replace(formula.right, old, new))

        if isinstance(formula, Implies):
            return Implies(self.replace(formula.left, old, new), self.replace(formula.right, old, new))

        return formula