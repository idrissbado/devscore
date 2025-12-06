# Installing devscore with Anaconda

## Quick Start with Conda

### Option 1: Create a new conda environment (Recommended)

```bash
# Create a new environment with Python 3.10+
conda create -n devscore python=3.10 -y
conda activate devscore

# Install dependencies via conda (faster, optimized binaries)
conda install -c conda-forge numpy pandas geopandas rasterio scikit-learn xgboost requests shapely pyproj -y

# Install remaining dependencies via pip
pip install osmnx h3 earthengine-api

# Install devscore
pip install devscore
```

### Option 2: Install in existing conda environment

```bash
# Activate your environment
conda activate your_env_name

# Install geospatial dependencies via conda
conda install -c conda-forge geopandas rasterio osmnx -y

# Install remaining dependencies
pip install h3 xgboost earthengine-api

# Install devscore
pip install devscore
```

### Option 3: Install from source in conda environment

```bash
# Create and activate environment
conda create -n devscore python=3.10 -y
conda activate devscore

# Install dependencies
conda install -c conda-forge numpy pandas geopandas rasterio scikit-learn xgboost shapely pyproj osmnx -y
pip install h3 earthengine-api requests

# Clone and install devscore
git clone https://github.com/idrissbado/devscore.git
cd devscore
pip install -e .
```

## Why Use Conda for Geospatial Packages?

Conda provides pre-compiled binaries for complex geospatial libraries like GDAL, GEOS, and PROJ, which can be difficult to compile from source. This makes installation faster and more reliable, especially on Windows.

**Key benefits:**
- Pre-built binaries for GDAL, rasterio, and geopandas
- Better dependency resolution for geospatial libraries
- Faster installation on Windows
- Consistent environment across platforms

## Troubleshooting

### Import errors after installation

If you encounter import errors:

```bash
# Reinstall geospatial stack via conda
conda install -c conda-forge --force-reinstall geopandas rasterio shapely pyproj
```

### GDAL version conflicts

```bash
# Check GDAL version
python -c "from osgeo import gdal; print(gdal.__version__)"

# If mismatched, reinstall via conda
conda install -c conda-forge gdal
```

### OSMnx network issues

```bash
# OSMnx requires network access
# Test connection
python -c "import osmnx as ox; print(ox.__version__)"
```

## Verifying Installation

```python
# Test basic imports
import devscore
from devscore import compute_development_score
from devscore.scoring.weights import WeightCalculator

print("✓ devscore installed successfully!")

# Test computation (requires internet)
lat, lon = -1.2921, 36.8219  # Nairobi, Kenya
try:
    result = compute_development_score(lat, lon, buffer_km=5)
    print(f"✓ Development score computed: {result['overall_score']:.3f}")
except Exception as e:
    print(f"Note: Full computation requires internet access: {e}")
```

## Jupyter Notebook Setup

```bash
# Install Jupyter in your conda environment
conda install -c conda-forge jupyter notebook ipykernel -y

# Register environment as Jupyter kernel
python -m ipykernel install --user --name devscore --display-name "Python (devscore)"

# Start Jupyter
jupyter notebook
```

Then select "Python (devscore)" as your kernel when creating a new notebook.

## Common Conda Commands

```bash
# List environments
conda env list

# Activate environment
conda activate devscore

# List installed packages
conda list

# Update all packages
conda update --all

# Export environment
conda env export > environment.yml

# Create environment from file
conda env create -f environment.yml

# Remove environment
conda env remove -n devscore
```

## Complete Environment File

Save this as `environment.yml`:

```yaml
name: devscore
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - numpy
  - pandas
  - geopandas
  - rasterio
  - scikit-learn
  - xgboost
  - shapely
  - pyproj
  - osmnx
  - jupyter
  - notebook
  - matplotlib
  - seaborn
  - pip
  - pip:
    - h3
    - earthengine-api
    - devscore
```

Create environment:
```bash
conda env create -f environment.yml
conda activate devscore
```
