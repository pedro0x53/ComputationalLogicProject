from Tableaux import *
from TimeAllocation import *
import time


# # Example 1
# # p → q, q → r, ¬(p → r)
# formula1 = Implies(Atom('p'), Atom('q'))
# formula2 = Implies(Atom('q'), Atom('r'))
# formula3 = Not(Implies(Atom('p'), Atom('r')))
# valuesFormulas1 = [1, 1, 1]
# formulas1 = [formula1, formula2, formula3]
# start_time = time.time()
# print()
# print(satisfiability_tableaux(start_time, formulas1, valuesFormulas1))
# end_time = time.time()
# print('Time:', end_time - start_time)
#
#
# # Example 2
# # p → q, q → r
# valuesFormulas2 = [1, 1]
# formulas2 = [formula1, formula2]
# start_time = time.time()
# print()
# print(satisfiability_tableaux(start_time, formulas2, valuesFormulas2))
# end_time = time.time()
# print('Time:', end_time - start_time)
#
#
# # Example 3
# # ((p ∨ q) ∧ (¬p ∧ ¬q))
# formula3 = And(Or(Atom('p'), Atom('q')), And(Not(Atom('p')), Not(Atom('q'))))
# formulas3 = [formula3]
# valuesFormulas3 = [1]
# start_time = time.time()
# print()
# print(satisfiability_tableaux(start_time, formulas3, valuesFormulas3))
# end_time = time.time()
# print('Time:', end_time - start_time)


#  Project
formula = getFormula()
# Verifying satisfiability
formulas4 = [formula]
valuesFormulas4 = [1]
start_time = time.time()
print()
print(satisfiability_tableaux(start_time, formulas4, valuesFormulas4, max_time=15))
end_time = time.time()
print('Time:', end_time - start_time)


# Verifying unsatisfiability - semester
formulas5 = [formula]
formulas5.append(And(Atom('s1_6_p0a_d0a'), Atom('s1_6_p1a_d1a')))
valuesFormulas5 = [1, 1]
start_time = time.time()
print()
print(satisfiability_tableaux(start_time, formulas5, valuesFormulas5))
end_time = time.time()
print('Time:', end_time - start_time)


# Verifying unsatisfiability -  professor
formulas6 = [formula]
formulas6.append(And(Atom('s1_3_p0a_d0a'), Atom('s2_3_p0a_d0b')))
valuesFormulas6 = [1, 1]
start_time = time.time()
print()
print(satisfiability_tableaux(start_time, formulas6, valuesFormulas6))
end_time = time.time()
print('Time:', end_time - start_time)


# Verifying unsatisfiability - schedule
formulas7 = [formula]
formulas7.append(And(Atom('s1_8_p0a_d0a'), Atom('s1_10_p0a_d0a')))
valuesFormulas7 = [1, 1]
start_time = time.time()
print()
print(satisfiability_tableaux(start_time, formulas7, valuesFormulas7))
end_time = time.time()
print('Time:', end_time - start_time)
