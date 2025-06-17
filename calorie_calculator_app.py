import streamlit as st
import json

# Load nutrition data
with open(r'C:\Users\ckeabetswe\source\repos\connectivity\calories_calculator\nutrition.json', 'r') as json_file:
    nutrition_dict = json.load(json_file)

# Function to compute nutritional summary
def nutritional_summary(foods):
    result_dict = {
        "Calories": 0, "Total Fat (g)": 0, "Protein (g)": 0,
        "Carbohydrate (g)": 0, "Sugars (g)": 0
    }
    for name, grams in foods.items():
        if name in nutrition_dict:
            nutrition = nutrition_dict[name]
            result_dict["Calories"] += grams * nutrition["calories"] / 100
            result_dict["Total Fat (g)"] += grams * nutrition["total_fat"] / 100
            result_dict["Protein (g)"] += grams * nutrition["protein"] / 100
            result_dict["Carbohydrate (g)"] += grams * nutrition["carbohydrate"] / 100
            result_dict["Sugars (g)"] += grams * nutrition["sugars"] / 100
        else:
            st.error(f"'{name}' not found in the nutrition database.")
            return None
    return result_dict

# Streamlit UI
st.title("🥗 Calorie Intake Calculator")

st.markdown("Enter food items and their amount (grams) to calculate total nutritional values.")

# Dynamic form
foods = {}
food_options = list(nutrition_dict.keys())

with st.form("nutrition_form"):
    num_items = st.number_input("How many different foods do you want to enter?", min_value=1, max_value=10, value=2)

    for i in range(num_items):
        col1, col2 = st.columns([2, 1])
        with col1:
            food = st.selectbox(f"Food #{i+1}", food_options, key=f"food_{i}")
        with col2:
            grams = st.number_input(f"Grams of {food}", min_value=0.0, step=10.0, key=f"grams_{i}")
        foods[food] = grams

    submitted = st.form_submit_button("Calculate")

# Show results
if submitted:
    summary = nutritional_summary(foods)
    if summary:
        st.subheader("🍽️ Nutritional Summary")
        for k, v in summary.items():
            st.write(f"**{k}**: {v:.2f}")
