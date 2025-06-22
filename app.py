from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_URL = "https://www.thecocktaildb.com/api/json/v1/1"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", current_year=datetime.now().year)

@app.route("/search", methods=["POST"])
def search():
    name = request.form.get("searchName")
    try:
        response = requests.get(f"{API_URL}/search.php?s={name}")
        result = response.json()
        drink = result.get("drinks", [None])[0]

        if not drink:
            return render_template("index.html", error="No drink found.")

        ingredients = [
            drink.get(f"strIngredient{i}")
            for i in range(1, 16)
            if drink.get(f"strIngredient{i}")
        ]

        return render_template("cocktailPage.html", drink=drink, ingredients=ingredients)
    except Exception as e:
        print("The request failed:", str(e))
        return render_template("index.html", error="Something went wrong! Please try again later.")

@app.route("/random", methods=["GET"])
def random_cocktail():
    try:
        response = requests.get(f"{API_URL}/random.php")
        result = response.json()
        drink = result.get("drinks", [None])[0]

        ingredients = [
            drink.get(f"strIngredient{i}")
            for i in range(1, 16)
            if drink.get(f"strIngredient{i}")
        ]

        return render_template("cocktailPage.html", drink=drink, ingredients=ingredients)
    except Exception as e:
        print("The request failed:", str(e))
        return render_template("index.html", error="Something went wrong! Please try again later.")

if __name__ == "__main__":
    app.run(debug=True, port=3000)
