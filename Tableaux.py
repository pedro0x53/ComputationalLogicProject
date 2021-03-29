from Formulas import *
import time


branches = []


def hasContradictions(premises):
    for formula in premises:
        neg_formula = Not(formula)
        if premises.__contains__(neg_formula):
            return True
    return False


def alpha_formulas(premise):
    if isinstance(premise, And):
        return [premise.left, premise.right]
    if isinstance(premise, AndAll):
        return premise.formulas_andAll()
    if isinstance(premise, Not) and isinstance(premise.inner, Not):
        return premise.inner.inner
    if isinstance(premise, Not) and isinstance(premise.inner, Or):
        return [Not(premise.inner.left), Not(premise.inner.right)]
    if isinstance(premise, Not) and isinstance(premise.inner, Implies):
        return [premise.inner.left, Not(premise.inner.right)]
    else:
        return None


def beta_formulas(premise):
    if isinstance(premise, Or):
        return [premise.left, premise.right]
    if isinstance(premise, Not) and isinstance(premise.inner, And):
        return [Not(premise.inner.left), Not(premise.inner.right)]
    if isinstance(premise, Implies):
        return [Not(premise.left), premise.right]


def isAtom_orNegAtom(premise):
    if isinstance(premise, Atom):
        return True
    if isinstance(premise, Not) and isinstance(premise.inner, Atom):
        return True
    else:
        return False


def verify_branches(branches, premises):
    # get the last tuple of array of tuples(branches)
    current_branch = branches.pop()
    # Verifies how much back on array of formulas and array of values
    positions_return = len(premises) - len(current_branch[0])

    for index in range(positions_return):
        premises.pop()

    # get values of formulas saved on tuple
    values_formulas = current_branch[0]
    # append formula saved on tuple
    premises.append(current_branch[1])

    # Verifying if a rule can be applied on formula from tuple
    if isAtom_orNegAtom(current_branch[1]):
        values_formulas.append(0)
    else:
        values_formulas.append(1)

    return values_formulas


def verifying_contradictions(branches, premises, valuesFormulas):
    # if current branch has contradictions and tuple has any branches. It's a closed branch
    if hasContradictions(premises) and branches != []:
        # print()
        # print(print_formulas(premises))
        new_valuesFormulas = verify_branches(branches, premises)
        # print("Closed Branch")
        return [True, new_valuesFormulas]

    # if current branch has contradictions and tuple hasn't any branches. It's a closed tableaux
    if hasContradictions(premises) and branches == []:
        # print()
        # print(print_formulas(premises))
        print("Closed Tableaux, the formula is insatisfiable")
        return [False, None]

    # if any rule can be applied and hasn't contradictions on branch. It's an open branch
    if not hasContradictions(premises) and branches != [] and not valuesFormulas.__contains__(1):
        # print()
        # print(print_formulas(premises))
        # new_valuesFormulas = verify_branches(branches, premises)
        print("Saturated and open branch - Open Tableaux, the formula is satisfiable")
        return [False, None]
        # return [True, new_valuesFormulas]

    # if hasn't branches and contradictions, and any rule can be applied. It's a open tableaux
    if not hasContradictions(premises) and branches == [] and not valuesFormulas.__contains__(1):
        # print()
        # print(print_formulas(premises))
        print("Open Tableaux, the formula is satisfiable")
        return [False, None]

    else:
        return None


def has_or(premisses, valuesFormulas):
    count = 0
    for formula in premisses:
        if isinstance(formula, Or):
            if valuesFormulas[count] == 1:
                return count
        count += 1


def print_formulas(formulas):
    for formula in formulas:
        print(formula)


def satisfiability_tableaux(start_time, formulas, valuesFormulas, existsBranches = True, max_time=10):
    while existsBranches:
        # Verifying contradictions (Premisses)
        result = verifying_contradictions(branches, formulas, valuesFormulas)

        # If not exists branches
        if result is not None and not result[0]:
            existsBranches = False
            break

        # If exists branches
        if result is not None and result[0]:
            valuesFormulas = result[1]
            count += 1
            continue

        else:
            # Apply rules
            # First on alpha formulas (do not fork)
            count = 0

            # Checking alpha formulas
            for formula in formulas:

                # Time of execution
                end_time = time.time()
                time_verification = (end_time - start_time) > max_time
                if time_verification:
                    existsBranches = False
                    break

                formulas_generated = alpha_formulas(formula)

                # Verifies if a rule can be applied
                if valuesFormulas[count] == 1:
                    if formulas_generated is None:
                        count += 1
                        continue

                    if formulas_generated is not None:
                        for formula in formulas_generated:

                            valuesFormulas[count] = 0

                            # Verifies if is an atom or an atom negation
                            formulas.append(formula)
                            if isAtom_orNegAtom(formula):
                                valuesFormulas.append(0)
                            else:
                                valuesFormulas.append(1)

                        # Verifying contradictions (After apply a rule)
                        result = verifying_contradictions(branches, formulas, valuesFormulas)

                        # If not exists branches
                        if result is not None and not result[0]:
                            existsBranches = False
                            break

                        # If exists branches
                        if result is not None and result[0]:
                            valuesFormulas = result[1]
                            count += 1
                            continue

                count += 1

            if time_verification:
                return print("Run time exceeded")
                break

            # Restart counting
            count = 0

            # Checking beta formulas (fork)
            for formula in formulas:

                # Time of execution
                end_time = time.time()
                time_verification = (end_time - start_time) > max_time
                if time_verification:
                    existsBranches = False
                    break

                if not existsBranches:
                    break

                # Verifying contradictions
                result = verifying_contradictions(branches, formulas, valuesFormulas)

                # If not exists branches
                if result is not None and not result[0]:
                    existsBranches = False
                    break

                # If exists branches
                if result is not None and result[0]:
                    valuesFormulas = result[1]
                    count += 1
                    continue

                # Applies or rules first
                if has_or(formulas, valuesFormulas) is not None:
                    count = has_or(formulas, valuesFormulas)
                    formulas_generated = beta_formulas(formulas[count])
                else:
                    # Return counting
                    count = formulas.index(formula)
                    formulas_generated = beta_formulas(formula)

                # Verifies if a rule can be applied
                if valuesFormulas[count] == 1:
                    if formulas_generated is None:
                        count += 1
                        continue

                    if formulas_generated is not None:
                        # for formula in formulas_generated:
                        formula = formulas_generated[0]

                        valuesFormulas[count] = 0

                        # Add branch
                        branches.append((valuesFormulas.copy(), formulas_generated[1]))

                        # Verifies if is an atom or an atom negation
                        formulas.append(formula)
                        if isAtom_orNegAtom(formula):
                            valuesFormulas.append(0)
                        else:
                            valuesFormulas.append(1)

                        # Verifying contradictions (After apply a rule)
                        result = verifying_contradictions(branches, formulas, valuesFormulas)

                        # If not exists branches
                        if result is not None and not result[0]:
                            existsBranches = False
                            break

                        # If exists branches
                        if result is not None and result[0]:
                            valuesFormulas = result[1]
                            count += 1
                            continue

                count += 1

            if time_verification:
                return print("Run time exceeded")
                break
