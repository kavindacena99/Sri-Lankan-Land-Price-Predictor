import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# CSV
df = pd.read_csv("land_data.csv")

# Handle missing values
df = df.dropna()

# Encode location string to numeric
le = LabelEncoder()
df['LocationEncoded'] = le.fit_transform(df['Location'])

# Features and target
X = df[['LocationEncoded', 'Size']]
y = df['Price']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model and encoder
joblib.dump(model, 'land_price_model.pkl')
joblib.dump(le, 'location_encoder.pkl')

# Test 
sample_location = 'Colombo'
sample_size = 10
encoded_loc = le.transform([sample_location])[0]
predicted_price = model.predict([[encoded_loc, sample_size]])
print(f"Predicted Price for {sample_size} perch land in {sample_location}: Rs {predicted_price[0]:,.2f}")

# check the accuarcy
y_pred = model.predict(X_test)

# Calculate metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Print results
print("\n📊 Model Evaluation:")
print(f"MAE : Rs {mae:,.2f}")
print(f"MSE : Rs {mse:,.2f}")
print(f"RMSE: Rs {rmse:,.2f}")
print(f"R² Score: {r2:.4f}")

