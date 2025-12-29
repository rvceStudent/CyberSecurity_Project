import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

from ml_model import AttackDetector

# -----------------------------
# Paths (ROOT SAFE)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "cicids.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_DIR, exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv(DATA_PATH)
data.columns = data.columns.str.strip()
print("✔ Dataset loaded")

# -----------------------------
# Features & Labels
# -----------------------------
features = [
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Flow Packets/s",
    "Flow Bytes/s"
]

X = data[features]
y = data["Label"].apply(lambda x: 0 if x == "BENIGN" else 1)

# -----------------------------
# Cleaning
# -----------------------------
X.replace([np.inf, -np.inf], np.nan, inplace=True)
X.dropna(inplace=True)
y = y.loc[X.index]
X = X.apply(pd.to_numeric)
X.fillna(X.mean(), inplace=True)

# -----------------------------
# Scaling
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, os.path.join(MODEL_DIR, "scaler.save"))

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, _, y_train, _ = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train.values, dtype=torch.float32)

# -----------------------------
# Model Training
# -----------------------------
model = AttackDetector()
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

EPOCHS = 20
for epoch in range(EPOCHS):
    optimizer.zero_grad()
    output = model(X_train).squeeze()
    loss = criterion(output, y_train)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}/{EPOCHS} | Loss: {loss.item():.4f}")

# -----------------------------
# Save Model
# -----------------------------
torch.save(model.state_dict(), os.path.join(MODEL_DIR, "attack_model.pth"))
print("✅ Model & scaler saved successfully")
