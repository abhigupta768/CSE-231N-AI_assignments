"""
utils.py: Utilities.
"""


from logic import *


def printTruthTable(form):
    """
    Print the truth table of the given formula.
    """

    if not isinstance(form, Formula):
        raise ValueError('Formula not valid.')

    print('Formula: %s' % form)
    
    atomsList = sorted(form.getAtoms())
    lengthList = []

    for i in atomsList:
        if len(i) < 5:
            lengthList.append(5)
        else:
            lengthList.append(len(i))
    lengthList.append(len('Truth Value'))
            
    totalWidth = sum(lengthList) + len(lengthList) + 1
        
    print('-' * totalWidth)
    print('|', end='')
    for i in range(len(atomsList)):
        print('%{0}s|'.format(lengthList[i]) % atomsList[i], end='')
    print('Truth Value|')
    print('-' * totalWidth)
    
    truthDict = {}
    
    for i in range(2 ** len(atomsList)):
        print('|', end='')
        
        for j in range(len(atomsList)):
            val = bool((i & (1 << j)) >> j)
            truthDict[atomsList[j]] = val
            
            print('%{0}s|'.format(lengthList[j]) % val, end='')
            
        truth = form.truthValue(truthDict)

        print('%{0}s|'.format(lengthList[-1]) % val)
        print('-' * totalWidth)

        
def areEquivalent(form1, form2):
    """
    For two formulas, find out whether they are equivalent.

    We do this by subtituting each atom for a truth value and
    checking whether for all combinations of truth values, the 
    truth value of the final expression becomes same.
    """

    if not isinstance(form1, Formula) or not isinstance(form2, Formula):
        raise ValueError('Formulas are not actually formulas.')

    atomsList = sorted(list(form1.getAtoms().union(form2.getAtoms())))
    
    truthDict = {}

    for i in range(2 ** len(atomsList)):
        for j in range(len(atomsList)):
            truthDict[atomsList[j]] = bool((i & (1 << j)) >> j)
            
        truth1 = form1.truthValue(truthDict)
        truth2 = form2.truthValue(truthDict)

        if truth1 != truth2:
            return False

    # All checks successful! Formulas are equivalent.
    return True


def isTautology(form):
    """
    Method to check whether the given formula is a tautology.
    """

    return Formula.areEquivalent(form, Atom('True'))


def isFallacy(form):
    """
    Method to check whether the given formula is a fallacy.
    """

    return Formula.areEquivalent(form, Atom('False'))
