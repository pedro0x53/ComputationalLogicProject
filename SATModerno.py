from pysat.solvers import Glucose3
from pysat.formula import CNF

def runPySAT():
	with open('CNF Files/Satisfactory/uf50-01.cnf', 'r') as file:
		cnf = CNF(from_fp = file)
		glucose = Glucose3()
		glucose.append_formula(cnf)
		print(glucose.solve())
