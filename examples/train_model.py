"""
Example: Train poverty prediction model with DHS data
"""

import numpy as np
import pandas as pd
from devscore.data import DHSDataHandler
from devscore.scoring.poverty import PovertyPredictor

print("Training Poverty Prediction Model")
print("="*60)

# Step 1: Load or generate DHS training data
print("\nStep 1: Loading DHS data...")
dhs_handler = DHSDataHandler()

# Generate synthetic data for demonstration
# In production, load actual DHS data
dhs_df = dhs_handler.generate_synthetic_dhs_data(n_samples=500, region='kenya')
print(f"Loaded {len(dhs_df)} DHS samples")

# Step 2: Simulate feature collection for DHS locations
print("\nStep 2: Simulating feature collection...")

# Create synthetic features matching DHS locations
np.random.seed(42)
n_samples = len(dhs_df)

features_dict = {
    'nightlights_norm': np.random.beta(2, 2, n_samples),
    'nightlights_raw': np.random.uniform(0, 100, n_samples),
    'ndvi': np.random.uniform(0.2, 0.7, n_samples),
    'ndbi': np.random.uniform(0, 0.4, n_samples),
    'buildup': np.random.uniform(0, 0.6, n_samples),
    'log_population': np.log1p(np.random.uniform(10, 5000, n_samples)),
    'amenity_density': np.random.uniform(0, 50, n_samples),
    'schools': np.random.randint(0, 20, n_samples),
    'health': np.random.randint(0, 10, n_samples),
    'road_density': np.random.uniform(0, 10, n_samples),
    'market_access': np.random.uniform(0, 1, n_samples),
}

X = pd.DataFrame(features_dict).values
y = dhs_df['wealth_index'].values

print(f"Feature matrix shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Step 3: Train model
print("\nStep 3: Training Random Forest model...")
predictor = PovertyPredictor()
metrics = predictor.train_model(X, y, model_type='random_forest')

print(f"\nTraining Results:")
print(f"  Train RMSE: {metrics['train_rmse']:.4f}")
print(f"  Test RMSE: {metrics['test_rmse']:.4f}")
print(f"  Train R²: {metrics['train_r2']:.4f}")
print(f"  Test R²: {metrics['test_r2']:.4f}")

# Step 4: Feature importance
print("\nStep 4: Feature Importance:")
print("-"*60)
importances = predictor.get_feature_importance()
sorted_features = sorted(importances.items(), key=lambda x: x[1], reverse=True)

for feature, importance in sorted_features[:5]:
    print(f"  {feature:20s}: {importance:.4f}")

# Step 5: Save model
print("\nStep 5: Saving model...")
predictor.save_model("poverty_model.pkl")
print("Model saved successfully!")

# Step 6: Test prediction
print("\nStep 6: Testing prediction on new location...")
test_features = np.array([[0.5, 50, 0.4, 0.2, 0.3, 6.0, 10, 5, 3, 2.5, 0.6]])
prediction = predictor.predict(test_features)
print(f"Predicted wealth index: {prediction:.3f}")
print(f"Predicted poverty score: {1-prediction:.3f}")
