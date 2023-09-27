import streamlit as st
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
# Load the dataset
df = sns.load_dataset("diamonds")
# Convert categorical variables to numerical
df["cut"] = df["cut"].astype("category").cat.codes
df["color"] = df["color"].astype("category").cat.codes
df["clarity"] = df["clarity"].astype("category").cat.codes
# Extract features and labels
X = df[['carat', 'cut', 'color', 'clarity']]
y = df["price"]
# train multiple models
models = {
    "Random Forest": RandomForestRegressor(n_estimators=100),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100)
}
for name, model in models.items():
    model.fit(X, y)
# create a streamlit app
st.title("ML app to predict Diamond price")
# Add sidebar for selecting a model
model_name = st.sidebar.selectbox("Select a Model", list(models.keys()))
selected_model = models[model_name]
# prediction
y_pred = selected_model.predict(X)
# calculate the model performance
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
# display the results to the user
st.subheader(model_name)
st.write(f'MSE: {mse:.2f}')
st.write(f'R2: {r2:.2f}')