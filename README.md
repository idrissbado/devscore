# devscore 🌍

**devscore** is a Python package that computes a multi-dimensional Development Score using open geospatial, satellite, and survey-based indicators. It is inspired by cutting-edge development economics research from MIT, Oxford, and the World Bank.

It helps researchers, governments, and NGOs estimate local well-being and market access for any region in Africa.

## Features

- **Poverty Prediction**: ML-based poverty estimation using satellite imagery, nightlights, and infrastructure data
- **Market Access**: Distance and travel time calculations to economic centers, markets, and key services
- **Infrastructure Mapping**: Density analysis of schools, hospitals, roads, and financial services from OSM
- **Food Security Assessment**: NDVI-based vegetation and agricultural productivity analysis
- **Night-time Lights**: Economic activity proxy using VIIRS satellite data
- **Mobile Money Potential**: Financial inclusion indicators

## Installation

```bash
pip install devscore
```

Or install from source:

```bash
git clone https://github.com/yourusername/devscore.git
cd devscore
pip install -e .
```

## Dependencies

```bash
pip install numpy pandas geopandas rasterio earthengine-api osmnx scikit-learn xgboost requests h3 shapely
```

## Quick Start

```python
from devscore import compute_development_score

# Compute development score for a location
lat, lon = -1.2921, 36.8219  # Nairobi, Kenya
score = compute_development_score(lat, lon)

print(f"Development Score: {score['overall']:.3f}")
print(f"  - Poverty Score: {score['poverty']:.3f}")
print(f"  - Market Access: {score['market_access']:.3f}")
print(f"  - Infrastructure: {score['infrastructure']:.3f}")
print(f"  - Food Security: {score['food_security']:.3f}")
print(f"  - Mobile Money: {score['mobile_money']:.3f}")
```

## Data Sources

All data sources are open and freely accessible:

- **Satellite Imagery**: Sentinel-2 (AWS Open Data), Landsat 8/9
- **Night-time Lights**: NOAA VIIRS DNB
- **Infrastructure**: OpenStreetMap via OSMnx
- **Population**: WorldPop
- **Wealth Data**: DHS (Demographic and Health Surveys)

## Methodology

The package implements a weighted aggregation of five key development indicators:

```
Development Score = 0.35 × Poverty + 0.20 × Market Access + 
                   0.20 × Infrastructure + 0.15 × Food Security + 
                   0.10 × Mobile Money
```

Each component is normalized to a 0-1 scale where 1 indicates highest development.

### Components

1. **Poverty Score**: Machine learning model trained on DHS wealth index, using features like nightlights, NDVI, built-up area, population density, and road density

2. **Market Access**: Exponential decay function based on distance to markets, roads, hospitals, and economic centers

3. **Infrastructure Index**: Density of amenities (schools, clinics, markets, banks) per km²

4. **Food Security**: NDVI-based vegetation health indicator

5. **Mobile Money**: Financial inclusion proxy based on agent density and connectivity

## Research Background

This package is inspired by academic research from:

- World Bank Development Economics (DEC)
- MIT Poverty Lab
- Oxford Centre for the Study of African Economies (CSAE)
- LSE International Growth Centre (IGC)
- Harvard Growth Lab
- Nature papers on satellite-based poverty prediction

## Citation

If you use this package in your research, please cite:

```bibtex
@software{devscore2025,
  title={devscore: A Python Package for Multi-dimensional Development Scoring},
  author={Idriss Olivier Bado},
  year={2025},
  url={https://github.com/idrissb/devscore}
}
```

## License

MIT License

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgments

Thanks to the open data community and organizations providing free access to geospatial data for development research.
