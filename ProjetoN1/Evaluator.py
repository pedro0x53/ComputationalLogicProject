from Formulas import *
from Utils import *


class Evaluator:
    # Evaluation Modes
    satisfactory = 1
    doubleSatisfactory = 2
    allModels = 3

    def __init__(self):
        pass

    def truthValueOf(self, formula, definition):
        if isinstance(formula, Atom):
            return definition.get(formula.name)

        if isinstance(formula, Not):
            return not self.truthValueOf(formula.inner, definition) if self.truthValueOf(formula.inner,
                                                                                         definition) != None else None

        if isinstance(formula, And):
            return self.truthValueOf(formula.left, definition) and self.truthValueOf(formula.right, definition)

        if isinstance(formula, Or):
            return self.truthValueOf(formula.left, definition) or self.truthValueOf(formula.right, definition)

        if isinstance(formula, Implies):
            if self.truthValueOf(formula.left, definition) == False or self.truthValueOf(formula.right,
                                                                                         definition) == True:
                return True
            elif self.truthValueOf(formula.left, definition) == True and self.truthValueOf(formula.right,
                                                                                           definition) == False:
                return False

        return None

    def satisfability(self, formula, mode=1):
        atoms = formula.atoms()  # Keys for the definition dictionary
        numberOfAtoms = len(atoms)
        numberOfEvaluations = 2 ** numberOfAtoms

        satisfactoryDefinitions = []

        for evaluation in range(numberOfEvaluations):
            binaryWord = integerToBinaryString(evaluation)  # Check Utils function

            evaluationValues = [stringToBoolean(bit) for bit in binaryWord]  # Check Utils function
            remainingValues = [False] * (
                        numberOfAtoms - len(evaluationValues))  # Getting the remaining values to match with atoms

            definitionValues = remainingValues + evaluationValues  # Values for the definition dictionary

            definition = dict(
                zip(atoms, definitionValues))  # Building a dictionary with atoms as Keys and definitionValues as Values

            if self.truthValueOf(formula, definition):
                satisfactoryDefinitions.append(definition)

            if (mode == self.satisfactory):
                if len(satisfactoryDefinitions) == 1:
                    return satisfactoryDefinitions[0]
            elif (mode == self.doubleSatisfactory):
                if len(satisfactoryDefinitions) == 2:
                    return satisfactoryDefinitions
            else:
                continue

        if (mode == self.allModels) and (len(satisfactoryDefinitions) > 0):
            return satisfactoryDefinitions
        return False
