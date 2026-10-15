def logic_gates(a, b):
    if a not in (0, 1) or b not in (0, 1):
        raise ValueError("Inputs must be 0 or 1")

    return {
        "AND":  a & b,
        "OR":   a | b,
        "NOT A": 1 - a,
        "NAND": 1 - (a & b),
        "NOR":  1 - (a | b),
        "XOR":  a ^ b,
        "XNOR": 1 - (a ^ b),
    }

print("A B | AND OR NOT-A NAND NOR XOR XNOR")
for a in (0, 1):
    for b in (0, 1):
        results = logic_gates(a, b)
        print(
            f"{a} {b} |  "
            f"{results['AND']}   {results['OR']}   "
            f"{results['NOT A']}     {results['NAND']}    "
            f"{results['NOR']}   {results['XOR']}   "
            f"{results['XNOR']}"
        )
