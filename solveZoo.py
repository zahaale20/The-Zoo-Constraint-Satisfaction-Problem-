# Alex Zaharia
# CPSC5610
# Assignment #2

from typing import Dict, List

# Variables: one per animal
animals = ["Lion", "Antelope", "Hyena", "EvilLion", "Hornbill", "Meerkat", "Boar"] # 7 animals

# Domains: all for every animal
enclosures = [1, 2, 3, 4]

# Checks whether two pen numbers are neighbors in the 1-2-3-4 line.
# (So Antelope can stay at least one fence away from hungry lions.)
def is_adjacent(a:int, b:int) -> bool:
    return abs(a-b) == 1

# Enforces all constraints 1-7
def enforce_constraints(partial: Dict[str, int], animal: str, enclosure: int) -> bool:
    g = partial.get # instead of partial.get("Lion")

    # 7. The LION is king, so he wants to be in enclosure 1.
    if animal == "Lion" and enclosure != 1:
        return False
    if "Lion" in partial and partial["Lion"] != 1:
        return False

    # 1. The LION and the EVIL LION hate each other, and do not want to be in the same enclosure.
    if animal == "EvilLion" and g("Lion") == enclosure:
        return False
    if animal == "Lion" and g("EvilLion") == enclosure:
        return False

    # 2. The MEERKAT and BOAR are best friends, and have to be in the same enclosure.
    if animal == "Meerkat" and g("Boar") not in (None, enclosure):
        return False
    if animal == "Boar" and g("Meerkat") not in (None, enclosure):
        return False

    # 3. The HYENA smells bad. Only the EVIL LION will share his enclosure.
    if animal == "Hyena":
        # if someone is already in `enclosure` and it's not EvilLion, false
        if any(a != "EvilLion" and g(a) == enclosure for a in animals):
            return False
    else:
        # if we’re placing someone other than EvilLion into the hyena pen, false
        if g("Hyena") == enclosure and animal != "EvilLion":
            return False

    # 4. The EVIL LION wants to eat the MEERKAT, BOAR, and HORNBILL.
    if animal == "EvilLion" and any(g(a) == enclosure for a in ["Hornbill", "Meerkat", "Boar"]):
        return False
    if animal in {"Hornbill", "Meerkat", "Boar"} and g("EvilLion") == enclosure:
        return False

    # 5. The LION and the EVIL LION want to eat the ANTELOPE so badly that 
    # the ANTELOPE cannot be in either the same enclosure or in an enclosure adjacent to the LION or EVIL LION.
    if animal == "Antelope":
        for hunter in ("Lion", "EvilLion"):
            if g(hunter) and (g(hunter) == enclosure or is_adjacent(g(hunter), enclosure)):
                return False
    if animal in {"Lion", "EvilLion"} and g("Antelope") is not None:
        if g("Antelope") == enclosure or is_adjacent(g("Antelope"), enclosure):
            return False

    # 6. The LION annoys the HORNBILL, so the HORNBILL doesn't want to be in the LION's enclosure.
    if (animal == "Hornbill" and g("Lion") == enclosure) or (animal == "Lion" and g("Hornbill") == enclosure):
        return False

    return True

# Performs a depth-first back-tracking search and records every assignment that satisfies all constraints.
def solve_zoo() -> List[Dict[str, int]]:
    solutions: List[Dict[str, int]] = []

    def backtrack(assignment: Dict[str, int], i: int = 0):
        # Goal test ─ all 7 animals assigned?  →  record a complete solution
        if i == len(animals): 
            solutions.append(assignment.copy())
            return
        
        animal = animals[i]  # Next variable/animal to assign an enclosure

        for enclosure in enclosures: # Iterate over domain
            if enforce_constraints(assignment, animal, enclosure): # Constraint Filter: screens each tentative move against all seven rules before we spend time exploring it any further
                assignment[animal] = enclosure # TRY – place the current animal in a candidate pen.
                backtrack(assignment, i + 1) # RECURSE – solve the smaller sub-problem with the remaining animals.
                del assignment[animal] # UNDO – remove the tentative choice so other pens can be tried.

    backtrack({})
    return solutions

if __name__ == "__main__":
    solutions = solve_zoo()
    print(f"{len(solutions)} possible solutions found:\n")
    for solution in solutions:
        print(solution)
