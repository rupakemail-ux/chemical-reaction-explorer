from flask import Flask, render_template, request, jsonify
import pandas as pd
import re
from chemlib import Compound, Reaction

# ✅ Initialize Flask app
app = Flask(__name__)

# Load CSV once when the server starts
df = pd.read_csv("reactions.csv")

def normalize(compound):
    """Remove leading coefficients and uppercase the compound string."""
    return re.sub(r'^\d+', '', compound.strip().upper())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/react", methods=["POST"])
def react():
    data = request.get_json()
    c1 = normalize(data["compound1"])
    c2 = normalize(data["compound2"])

    product = "Unknown Product"
    balanced = ""

    try:
        query1 = f"{c1} + {c2}"
        query2 = f"{c2} + {c1}"

        # Normalize CSV reactants
        df["reactants_norm"] = df["reactants"].str.upper()
        row = df[(df["reactants_norm"] == query1) | (df["reactants_norm"] == query2)]

        if not row.empty:
            product = row.iloc[0]["products"]

            # Build compounds for balancing
            reactants_list = query1.split(" + ")
            products_list = product.split(" + ")

            reactants = {Compound(r): 1 for r in reactants_list}
            products = {Compound(p): 1 for p in products_list}

            reaction = Reaction(reactants, products)
            reaction.balance()
            balanced = reaction.formula

    except Exception:
        # Suppress error details, just leave balanced blank
        balanced = ""

    return jsonify({"result": product, "balanced": balanced})

if __name__ == "__main__":
    # ✅ Important for deployment: host=0.0.0.0
    app.run(host="0.0.0.0", port=5000, debug=True)
