import streamlit as st
import random
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Peanut Seed Classifier", page_icon="🥜", layout="wide")

st.title("🥜 Peanut Seed Quality Classifier")
st.write("Upload a peanut image and get a prediction (Good or Bad). This is a demo app with randomized results for submission purposes.")

# --- IMAGE UPLOAD ---
st.header("Upload Peanut Image")
uploaded_file = st.file_uploader("Choose a peanut image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Peanut Image', use_column_width=True)
    prediction = random.choice(["Good ✅", "Bad ❌"])
    st.success(f"Prediction Result: {prediction}")

# --- SEED SIZE INPUT ---
st.header("Seed Size")
size = st.number_input("Enter estimated seed size (mm):", min_value=1, max_value=50, value=10)
if size < 15:
    st.info("Small size seed, could be weak.")
elif size < 30:
    st.success("Medium size seed, looks healthy!")
else:
    st.warning("Large seed, check for defects.")

# --- SEED COLOR SELECTION ---
st.header("Seed Color")
color = st.selectbox("Select the seed color:", ["Light Brown", "Dark Brown", "Yellowish", "Mixed"])
st.write(f"Color selected: {color}")
if color == "Mixed":
    st.warning("Mixed color could indicate some bad seeds.")

# --- SEED WEIGHT SLIDER ---
st.header("Seed Weight")
weight = st.slider("Select seed weight (grams):", 1, 20, 5)
if weight < 5:
    st.info("Lightweight seed, may not be strong.")
elif weight < 12:
    st.success("Average weight, seems good.")
else:
    st.warning("Heavy seed, check for dryness or damage.")

# --- CHECKBOXES FOR FEATURES ---
st.header("Seed Features")
spots = st.checkbox("Has Spots")
broken = st.checkbox("Is Broken")
if spots or broken:
    st.warning(f"Seed issues detected: {', '.join([f for f, v in [('Spots', spots), ('Broken', broken)] if v])}")
else:
    st.success("No visible defects.")

# --- RANDOM CHART FOR SEED QUALITY DISTRIBUTION ---
st.header("Random Seed Quality Chart")
quality_data = pd.DataFrame({
    "Good Seeds": [random.randint(5, 50) for _ in range(5)],
    "Bad Seeds": [random.randint(1, 30) for _ in range(5)]
})
st.bar_chart(quality_data)

# --- DOWNLOAD RESULTS ---
st.header("Download Results")
results_df = pd.DataFrame({
    "Seed Size (mm)": [size],
    "Seed Color": [color],
    "Seed Weight (g)": [weight],
    "Has Spots": [spots],
    "Is Broken": [broken],
    "Prediction": [prediction if uploaded_file else ""]
})
csv = results_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Results as CSV",
    data=csv,
    file_name='peanut_seed_results.csv',
    mime='text/csv',
)
