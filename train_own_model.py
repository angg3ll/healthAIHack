import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

data = pd.read_csv('your_data.csv')  # Adjust file path
print(data.head())

def one_hot_encode(sequence, length=60):
    encoding = np.zeros((length, 4))  # 4 bases (A, T, C, G)
    base_map = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
    for i, base in enumerate(sequence[:length]):
        encoding[i, base_map.get(base, 0)] = 1
    return encoding.flatten()

data['encoded'] = data['sequence'].apply(one_hot_encode)

scaler = MinMaxScaler()
data[['P90', 'N10', 'Diff']] = scaler.fit_transform(data[['P90', 'N10', 'Diff']])

# # Prepare features and labels
# X = np.vstack(data['encoded'].values)
# y = data[['P90', 'N10', 'Diff']].values
#
# # Split into train/test
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Train Random Forest Regressor
# rf_model = RandomForestRegressor(n_estimators=100)
# rf_model.fit(X_train, y_train)
#
# # Evaluate
# print(f"Train R^2: {rf_model.score(X_train, y_train)}")
# print(f"Test R^2: {rf_model.score(X_test, y_test)}")

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create the model
model = Sequential([
    Dense(128, input_dim=X_train.shape[1], activation='relu'),
    Dense(64, activation='relu'),
    Dense(3, activation='linear')  # Output layer for P90, N10, Diff
])

model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Evaluate
model.evaluate(X_test, y_test)
