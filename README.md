# 🦁 Zoo Enclosure CSP Solver

**Author:** Alex Zaharia  
**Course:** CPSC 5610 – Artificial Intelligence  
**Assignment:** Homework #2  

This Python program solves a constraint satisfaction problem (CSP) involving the placement of seven zoo animals into four enclosures, under a unique and complex set of constraints. It uses depth-first backtracking with constraint filtering to find all valid configurations that satisfy the rules of the zoo.

---

## 🧠 Problem Overview

There are **7 animals**:
- Lion
- Antelope
- Hyena
- Evil Lion
- Hornbill
- Meerkat
- Boar

And **4 enclosures**: `1, 2, 3, 4` (arranged linearly)

### Constraints:
- **Lion vs. Evil Lion**: Cannot share the same enclosure.
- **Meerkat and Boar**: Must be together in the same enclosure.
- **Hyena**: Can only share an enclosure with the Evil Lion.
- **Evil Lion**: Cannot be placed with Meerkat, Boar, or Hornbill.
- **Antelope**: Must be at least one fence away from both Lions.
- **Hornbill**: Refuses to share an enclosure with the Lion.
- **Lion**: Must be placed in Enclosure 1 (he’s king, after all).

---

## 🔍 How It Works

- **Backtracking Search** is used to explore all possible combinations.
- The `enforce_constraints()` function filters out invalid placements early.
- When a complete, valid assignment is found, it is stored and printed.

---

## 📄 Example Output

{'Lion': 1, 'Antelope': 3, 'Hyena': 2, 'EvilLion': 2, 'Hornbill': 4, 'Meerkat': 1, 'Boar': 1} {'Lion': 1, 'Antelope': 3, 'Hyena': 4, 'EvilLion': 4, 'Hornbill': 2, 'Meerkat': 1, 'Boar': 1} ...
