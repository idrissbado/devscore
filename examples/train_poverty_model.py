"""
Example: Train poverty prediction model with DHS data
"""

from devscore.data import load_dhs_training_data, get_satellite_features, get_nightlights
from devscore.scoring.poverty import PovertyPredictor
import numpy as np

print("Training poverty prediction model...\n")

# Load or generate DHS data
print("Step 1: Loading DHS data...")
dhs_data = load_dhs_training_data(country='KE', year=2020)
print(f"Loaded {len(dhs_data)} DHS records\n")

# Create feature matrix
print("Step 2: Extracting features for training...")
X = []
y = []

# Sample subset for faster demo
sample_size = min(100, len(dhs_data))
dhs_sample = dhs_data.sample(n=sample_size, random_state=42)

for idx, row in dhs_sample.iterrows():
    lat = row['latitude']
    lon = row['longitude']
    wealth_index = row['wealth_index']
    
    # Get features
    try:
        satellite = get_satellite_features(lat, lon)
        nightlights = get_nightlights(lat, lon)
        
        # Construct feature vector
        features = [
            nightlights.get('intensity_normalized', 0),
            nightlights.get('intensity', 0),
            satellite.get('ndvi', 0),
            satellite.get('ndbi', 0),
            satellite.get('buildup_index', 0),
            0,  # population (placeholder)
            0,  # amenity density (placeholder)
            0,  # schools (placeholder)
            0,  # health (placeholder)
            0,  # road density (placeholder)
            0.5,  # market access (placeholder)
        ]
        
        X.append(features)
        y.append(wealth_index)
        
    except Exception as e:
        print(f"Error processing ({lat}, {lon}): {e}")
        continue

X = np.array(X)
y = np.array(y)

print(f"Created training dataset: {len(X)} samples with {X.shape[1]} features\n")

# Train model
print("Step 3: Training model...")
predictor = PovertyPredictor()
metrics = predictor.train_model(X, y, model_type='random_forest')

print("\nTraining Metrics:")
print(f"  Train R²: {metrics['train_r2']:.3f}")
print(f"  Test R²: {metrics['test_r2']:.3f}")
print(f"  Test RMSE: {metrics['test_rmse']:.3f}")

# Save model
print("\nStep 4: Saving model...")
predictor.save_model("poverty_model.pkl")

print("\n✓ Model training complete!")
