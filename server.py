from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open("reactions.json") as f:
    reactions = json.load(f)

def balance_equation(reactants, products):
    return f"{' + '.join(reactants)} → {' + '.join(products)}"

def simulate_reaction(comp1, comp2):
    key1 = f"{comp1}+{comp2}"
    key2 = f"{comp2}+{comp1}"
    if key1 in reactions:
        r = reactions[key1]
    elif key2 in reactions:
        r = reactions[key2]
    else:
        return "No reaction found."
    equation = balance_equation([comp1, comp2], r["products"])
    return f"Reaction type: {r['type']} | Equation: {equation}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/react", methods=["POST"])
def react():
    data = request.json
    comp1 = data["compound1"]
    comp2 = data["compound2"]
    result = simulate_reaction(comp1, comp2)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
