# Conjuctive Normal Formula
import re
from Formulas import *

class CNF:

	def __init__(self):
		pass


	def readCNFFile(self, filePath):
		clauses = set()
		with open(filePath, 'r') as file:
			for line in file:
				line = line.rstrip().lstrip()
				clauseMatch = re.search('^(-?\d+ +)+0$', line)
				if clauseMatch is not None:
					newLiterals = clauseMatch.string.split()
					del newLiterals[-1]

					newClause = set()
					for literal in newLiterals:
						newClause.add(int(literal))

					clauses.add(frozenset(newClause))

		return clauses


	def writeCNFFile(self, formula):
		pass


	def isValid(self, filePath):
		clauses = self.readCNFFile(filePath)
		for clause in clauses:
			isValid = False
			for literal in clause:
				if (literal * -1) in clause:
					isValid = True
					break
			if not isValid:
				return False
		return True


	def CNFFileToFormula(self, filePath):
		clauses = self.readCNFFile(filePath)
		return self.CNFClausesToFormula(clauses)


	def CNFClausesToFormula(self, clauses):
		formula = None

		for clause in clauses:

			clauseList = list(clause)

			clauseFormula = None

			if len(clauseList):
				firstLiteral = clauseList[0]
				clauseList.remove(firstLiteral)

				clauseFormula = Atom('p' + str(firstLiteral))

				if firstLiteral < 0:
					clauseFormula = Not(Atom('p' + str(firstLiteral * -1)))
			else:
				continue

			for literal in clauseList:
				literalFormula = Atom('p' + str(literal))
				
				if literal < 0:
					literalFormula = Not(Atom('p' + str(literal * -1)))

				clauseFormula = Or(clauseFormula, literalFormula)

			if formula == None:
				formula = clauseFormula
			else:
				formula = And(formula, clauseFormula)

		return formula


	def formulaToCNFClauses(self, formula):
		# get every atoms as string
		atoms = formula.atoms()

		# generate a enumerated dictionary from atoms set
		literalsToAtoms = dict(enumerate(atoms, 1))

		# get the reverse reference (key:value -> value:key)
		atomsToLiterals = {v: k for k, v in literalsToAtoms.items()}

		# transform formula to CNF format
		cnfFormula = self.formulaToCNFFormula(formula)

		# get the cnf formated formula as string
		cnfFormulaString = str(cnfFormula)

		# remove every parenthesis
		cnfFormulaString = cnfFormulaString.replace(")", "").replace("(", "")

		# Separete every clause by spliting on And string
		clausesStringGrouped = cnfFormulaString.split(u"\u2227")

		alphaClauses = set()
		# Separete every literal by spliting on Or string
		for clauseString in clausesStringGrouped:
			clauseSplited = clauseString.split(u"\u2228")
			newAlphaClause = frozenset([alphaLiteral.strip() for alphaLiteral in clauseSplited])

			alphaClauses.add(newAlphaClause)
		
		clauses = set()
		for alphaClause in alphaClauses:
			clause = set()
			for atom in alphaClause:
				if atom[0] == Not.unicodeString:
					clause.add(atomsToLiterals.get(atom[1:]) * -1)
				else:
					clause.add(atomsToLiterals.get(atom))

			clauses.add(frozenset(clause))

		return {"relation": literalsToAtoms, "clauses": clauses}



	def formulaToCNFFormula(self, formula):
		edformula = self.__removeImplications(formula)
		edformula = self.__removeNegation(edformula)
		edformula = self.__distributive(edformula)

		return edformula


	def __removeImplications(self, formula):
		if isinstance(formula, Not):
			return Not(self.__removeImplications(formula.inner))

		if isinstance(formula, And):
			return And(self.__removeImplications(formula.left), self.__removeImplications(formula.right))

		if isinstance(formula, Or):
			return Or(self.__removeImplications(formula.left), self.__removeImplications(formula.right))

		if isinstance(formula, Implies):
			return Or(Not(self.__removeImplications(formula.left)), self.__removeImplications(formula.right))

		return formula


	def __removeNegation(self, formula):
		if isinstance(formula, Not):
			if isinstance(formula.inner, Not):
				return self.__removeNegation(formula.inner.inner)

			if isinstance(formula.inner, And):
				return Or(self.__removeNegation(Not(formula.inner.left)), self.__removeNegation(Not(formula.inner.right)))

			if isinstance(formula.inner, Or):
				return And(self.__removeNegation(Not(formula.inner.left)), self.__removeNegation(Not(formula.inner.right)))

		if isinstance(formula, And):
			return And(self.__removeNegation(formula.left), self.__removeNegation(formula.right))

		if isinstance(formula, Or):
			return Or(self.__removeNegation(formula.left), self.__removeNegation(formula.right))

		return formula


	def __distributive(self, formula):
		if isinstance(formula, And):
			return And(self.__distributive(formula.left), self.__distributive(formula.right))

		if isinstance(formula, Or):
			if isinstance(formula.left, And):
				return And(
						Or(self.__distributive(formula.left.left), formula.right),
						Or(self.__distributive(formula.left.right), formula.right)
					   )

			if isinstance(formula.right, And):
				return And(
						Or(self.__distributive(formula.right.left), formula.left),
						Or(self.__distributive(formula.right.right), formula.left)
					   )

			return Or(self.__distributive(formula.left), self.__distributive(formula.right))

		return formula
