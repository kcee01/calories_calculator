# 🥗 Calories Intake Calculator

The **Calories Intake Calculator** is a Python-based tool that lets users easily calculate their total calorie and nutrient intake based on the foods they consume. It uses a local `nutrition.json` file as its data source and offers a clean, interactive **web interface built with Streamlit**.

---

## 🚀 Features

* ✅ Select multiple food items from a dropdown list
* ✅ Input weight (in grams) for each item
* ✅ Real-time calculation of:

  * Total Calories
  * Protein
  * Total Fat
  * Carbohydrates
  * Sugars
* ✅ Simple, responsive UI with Streamlit
* ✅ Nutrition data stored locally in `nutrition.json`

---

## ⚙️ How to Use

### 1. Clone the repository

```bash
git clone https://github.com/your-username/calories_calculator.git
cd calories_calculator
```

### 2. Install dependencies

```bash
pip install streamlit
```

### 3. Run the app

```bash
streamlit run calories_calculator_app.py
```

Then open the provided URL in your browser (usually [http://localhost:8501](http://localhost:8501)).

---

## 📊 Data Format (`nutrition.json`)

The app expects the nutrition data to be structured like this:

```json
{
  "country": "Botswana",
  "traditional_foods": [
    {
      "name": "Seswaa",
      "description": "Shredded beef or goat meat, slow-cooked and seasoned with salt.",
      "nutrition_per_100g": {
        "calories": 250,
        "protein": 26,
        "fat": 15,
        "carbohydrates": 0
      }
    },
    {
      "name": "Pap (Bogobe)",
      "description": "Thick maize meal porridge, often served with meat or vegetables.",
      "nutrition_per_100g": {
        "calories": 110,
        "protein": 2,
        "fat": 0.5,
        "carbohydrates": 24
      }
    },
    {
      "name": "Morogo (Wild Spinach)",
      "description": "Leafy green vegetable, similar to spinach, often boiled or sautéed.",
      "nutrition_per_100g": {
        "calories": 35,
        "protein": 3.5,
        "fat": 0.4,
        "carbohydrates": 4
      }
    }
  ]
}

```

> All values are per 100 grams.

---

## 🔧 Customization

You can expand the app by:

* Adding more foods to `nutrition.json`
* Implementing fuzzy search/autocomplete
* Adding charts (e.g. macronutrient pie chart)
* Deploying on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE) — feel free to use and adapt it!

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to improve or expand the app, feel free to fork it, submit a PR, or open an issue.


