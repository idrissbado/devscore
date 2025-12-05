# devscore Quick Start Guide

## Installation

```bash
cd devscore
pip install -e .
```

## Quick Example

```python
from devscore import compute_development_score

# Compute score for any location
lat, lon = -1.2921, 36.8219  # Nairobi, Kenya
score = compute_development_score(lat, lon)

print(f"Development Score: {score['overall']:.3f}")
print(f"Components:")
for name, value in score['components'].items():
    print(f"  {name}: {value:.3f}")
```

## Running Examples

```bash
cd examples
python basic_usage.py
python component_scores.py
python train_model.py
```

## Package Structure

```
devscore/
├── data/           # Data collection modules
├── scoring/        # Scoring algorithms
├── utils/          # Utility functions
└── __init__.py
```

## Key Features

- **5 Development Indicators**: Poverty, Market Access, Infrastructure, Food Security, Mobile Money
- **Open Data Sources**: Sentinel-2, VIIRS, OSM, WorldPop, DHS
- **ML-Based**: Trainable poverty prediction with Random Forest/XGBoost
- **Geospatial**: Full spatial analysis with buffer zones and distance calculations

Author: Idriss Olivier Bado
