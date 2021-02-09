from Formulas import *
from Evaluator import *


def main():
	evaluator = Evaluator()

	atomP = Atom("p")
	atomQ = Atom("q")
	atomR = Atom("r")
	atomR = Atom("r")

	formula1 = Not(atomR) 			  # ~r
	formula2 = And(atomP, atomQ) 	  # p ^ q
	formula3 = Or(atomP, atomR) 	  # p v r
	formula4 = Implies(atomP, atomR)  # p -> r
	formula5 = And(atomP, Not(atomP)) # p ^ ~p

	atomSatisfability = evaluator.satisfability(atomP, mode=Evaluator.satisfactory)
	notSatisfability = evaluator.satisfability(formula1, mode=Evaluator.satisfactory)
	andSatisfability = evaluator.satisfability(formula2, mode=Evaluator.satisfactory)
	orDoubleSatisfactory = evaluator.satisfability(formula3, mode=Evaluator.doubleSatisfactory)
	impliesAllModels = evaluator.satisfability(formula4, mode=Evaluator.allModels)
	unsatisfactory = evaluator.satisfability(formula5, mode=Evaluator.satisfactory)

	print(atomSatisfability)
	print(notSatisfability)
	print(andSatisfability)
	print(orDoubleSatisfactory)
	print(impliesAllModels)
	print(unsatisfactory)


if __name__ == "__main__":
	main()