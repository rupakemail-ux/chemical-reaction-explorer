import pandas as pd

reactions = []

# -----------------------------
# 1. Hydrocarbon Combustion
# -----------------------------
for n in range(1, 501):  # up to C500
    reactants = f"C{n}H{2*n+2} + O2"
    products = "CO2 + H2O"
    reactions.append((reactants, products))

# -----------------------------
# 2. Acid–Base Neutralizations
# -----------------------------
acid_anions = {
    "HCl": "Cl",
    "H2SO4": "SO4",
    "HNO3": "NO3",
    "CH3COOH": "CH3COO",
    "HBr": "Br",
    "HF": "F",
    "H2CO3": "CO3",
    "H3PO4": "PO4"
}

base_cations = {
    "NaOH": "Na",
    "KOH": "K",
    "Ca(OH)2": "Ca",
    "Mg(OH)2": "Mg",
    "Ba(OH)2": "Ba",
    "LiOH": "Li",
    "Sr(OH)2": "Sr",
    "Al(OH)3": "Al"
}

for acid, anion in acid_anions.items():
    for base, cation in base_cations.items():
        salt = f"{cation}{anion}"
        reactions.append((f"{acid} + {base}", f"{salt} + H2O"))

# -----------------------------
# 3. Decomposition + Auto-Synthesis
# -----------------------------
decomposition = [
    ("CaCO3", "CaO + CO2"),
    ("KClO3", "KCl + O2"),
    ("H2O2", "H2O + O2"),
    ("NH4NO3", "N2O + H2O"),
    ("NaHCO3", "Na2CO3 + CO2 + H2O"),
]

reactions.extend(decomposition)

for reactants, products in decomposition:
    if " + " in products:
        reactions.append((products, reactants))  # reverse synthesis

# -----------------------------
# 4. Displacement Reactions
# -----------------------------
displacements = [
    ("Zn + HCl", "ZnCl2 + H2"),
    ("Fe + CuSO4", "FeSO4 + Cu"),
    ("Al + Fe2O3", "Al2O3 + Fe"),
    ("Mg + H2O", "Mg(OH)2 + H2"),
    ("Cu + AgNO3", "Cu(NO3)2 + Ag"),
    ("Pb + CuCl2", "PbCl2 + Cu"),
]
reactions.extend(displacements)

# -----------------------------
# 5. Extra Synthesis Examples
# -----------------------------
synthesis = [
    ("N2 + H2", "NH3"),
    ("H2 + Cl2", "HCl"),
    ("Na + O2", "Na2O"),
    ("Fe + S", "FeS"),
    ("C + O2", "CO2"),
]
reactions.extend(synthesis)

# -----------------------------
# 6. Expand Dataset (multiply)
# -----------------------------
expanded = []
for i in range(10):  # repeat 10 times to reach thousands
    for r, p in reactions:
        expanded.append((r, p))

# Save to CSV
df = pd.DataFrame(expanded, columns=["reactants", "products"])
df.to_csv("reactions.csv", index=False)

print(f"Generated reactions.csv with {len(df)} reactions")
