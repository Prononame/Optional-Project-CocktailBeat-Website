Here’s a simple, clear **GitHub README** template including installation, usage, and features — all concise and beginner-friendly:

---

# CocktailBeat

CocktailBeat is a Flask web app that lets you search for cocktails or get random cocktail recipes using TheCocktailDB API. It shows ingredients, instructions, and images in a clean interface.

## Features

* Search cocktails by name
* Get random cocktail suggestions
* View ingredients, category, and instructions
* Responsive and user-friendly design

## Installation

1. **Clone the repo:**

   ```bash
   git clone https://github.com/yourusername/cocktailbeat.git
   cd cocktailbeat
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate   # macOS/Linux
   env\Scripts\activate      # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. Open your browser and go to:
   `http://localhost:3000`

3. Use the search bar to find cocktails or click the random button for a surprise.

## Requirements

* Python 3.6+
* Flask
* requests

## License

This project is licensed under the MIT License.
