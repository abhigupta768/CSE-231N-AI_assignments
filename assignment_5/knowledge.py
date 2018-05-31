"""
knowledge_base.py: Implements the knowledge base and resolution-refutation.
"""


from logic import *


def __simplifyORList(orList):
    """
    Simplify an elementary list of disjunctions.

    Eg. [A, ~A, B, B] => [B]
    """

    subList = []

    for r in orList:
        if r not in subList:
            subList.append(r)

    return subList


def __simplifyANDList(andList):
    """
    Simplify a CNF list.

    Eg. [[A, B, A], [~A, C, A]] => [[A, B], [C]]
    """

    simplifiedList = []

    for rs in andList:
        subList = __simplifyORList(rs)

        if subList not in simplifiedList:
            simplifiedList.append(subList)

    return simplifiedList


def __simplifyCNFList(formula):
    """
    This functions converts a formula into a list based CNF representation.
    Eg. (A v B) ^ (~A v ~C) is converted to a list of list of disjunctions
    like [[Atom(A), Atom(B)], [Not(Atom(A)), Not(Atom(C))]]. A few simplifications
    are also performed. Like A V A => A, A V True = True, etc..

    This functions returns a simplified list of lists.

    NOTE - This function assumes that all the toCNF() functions in logic.py are complete and correct.
    """
    formula = formula.toCNF()

    if not isinstance(formula, And):
        xs = [formula]
    else:
        xs = formula.flattenArgs()

    ys = list(map(lambda x: [x] if not isinstance(x, Or) else x.flattenArgs(), xs))

    return __simplifyANDList(ys)


def __applyResolution(resList, idx, quiet=False):
    """
    Apply one iteration of resolution algorithm.abs

    @resList: The simplified list of conjunstions after applying CNF.
              Eg. The formula (A v B) ^ (A V ~B) will be represented as
              [[A, B], [A, Not(B)]]
    @idx: the step number we are currently on (for the proof),
          simply, if this function is being called for the kth time,
          idx = k.
    @quiet: Whether to print outputs.

    returns: A new list of resolutions after applying resolution rule.
             If the rule couldn't be applied, return the original list.
    """

    # BEGIN YOUR CODE HERE #

    # Apply one iteration of the resolution refutation process
    # and return a new list containing the modified resolutions
    # in the same format.
    #
    # NOTE: 1. Don't forget to call __simplifyANDList on the final list!
    #       2. And don't modify the original list, make copies and return!
    #       3. Print the applied resolution step. If you combine X and Y to yeild Z,
    #          then print them to show how the proof proceeds.
    newResList = []
    newList=resList.copy()
    newResList = resList.copy()
    flag=0
    from itertools import combinations
    temp=list(combinations(newList,2))
    for comb in temp:
        for prop in comb[0]:
            if Not(prop).toCNF() in comb[1]:
                y=[]
                y+=comb[0]
                y+=comb[1]
                y.remove(prop)
                y.remove(Not(prop).toCNF())
                if y not in newResList:
                    newResList.append(y)
                    if not quiet:
                        print("{}: {} is derived from {} and {}".format(idx,y,comb[0],comb[1]))
                    flag=1
                    break
        if(flag==1):
            break
    return __simplifyANDList(newResList)

    # Or if we could't simplify the list further, return the original list

    # END YOUR CODE #


def resolutionRefutation(axioms, proposition, quiet=False):
    """
    @axioms(type = formula): These form the given premises
    @propositiontype = formula): To prove using the axioms
    @quiet: Controls the wordiness of output

    returns: Displays initial resolution formula, and final status after
             applying resolution-refutation (theorem proven or not).
    """

    if not isinstance(axioms, Formula) or not isinstance(proposition, Formula):
        raise TypeError('Given axioms or proposition not a valid formula.')

    if not quiet:
        print('Axioms: %s' % axioms)
        print('Proposition: %s' % proposition)

    # BEGIN YOUR CODE HERE #

    # Transform the axioms

    # Here combine the axiom and proposition to
    # prepare for resolution refutation
    resolutions = And(axioms,Not(proposition))

    # END YOUR CODE #

    oldRes = __simplifyCNFList(resolutions)
    if not quiet:
        print('Initial resolutions formula: %s' % resolutions)

    idx = 1
    while True:

        # BEGIN YOUR CODE #

        # Apply one step of resolution-refutation process
        # using the function __applyResolution on oldRes
        # with proper arguments
        newRes = __applyResolution(oldRes,idx,quiet)
        # END YOUR CODE #

        # Conditions to end the process

        # If an empty list occurs in the list of resulutions,
        # that means a refutation has been derived.
        # Check the functions _simplify*List above for details on why
        if [] in newRes:
            if not quiet:
                print('Final resolution list: %s' % And.fromList(list(map(lambda x: Or.fromList(x), newRes))))
                print('Contradiction! The given proposition follows from the axioms.')

            return True

        # If no change occurs in the resolution list then no
        # further steps can be performed
        elif newRes == oldRes:
            if not quiet:
                print('Final resolution list: %s' % And.fromList(list(map(lambda x: Or.fromList(x), newRes))))
                print('The given proposition is independent of the axioms.')
            return False

        oldRes = newRes
        idx += 1
