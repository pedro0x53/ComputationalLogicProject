from pysat.solvers import Glucose3
from pysat.formula import CNF


class SATModerno_fromFile:
	def __init__(self):
		pass

	def runPySAT_fromFile(self, file):
		with open(file, 'r') as file:
			cnf = CNF(from_fp = file)
			glucose = Glucose3()
			glucose.append_formula(cnf)

			if glucose.solve():
				return glucose.get_model()
			else:
				return False