"""
Example: Analyze a specific component - Food Security
"""

from devscore.data import get_satellite_features, get_population_density
from devscore.scoring.food_security import FoodSecurityScorer

# Location: Rural area in Ethiopia
lat = 9.0
lon = 38.75

print(f"Analyzing food security for location ({lat}, {lon})...\n")

# Collect data
print("Collecting satellite data...")
satellite_data = get_satellite_features(lat, lon, buffer_km=10)

print("Collecting population data...")
population_data = get_population_density(lat, lon)

# Compute food security
print("\nComputing food security score...")
scorer = FoodSecurityScorer()
result = scorer.compute_food_security_score(satellite_data, population_data)

# Display results
print("\n" + "="*60)
print("FOOD SECURITY ANALYSIS")
print("="*60)
print(f"\nLocation: ({lat}, {lon})")
print(f"Overall Score: {result['score']:.3f}")
print(f"Classification: {result['classification']}")
print(f"Risk Level: {result['risk_level']}")

print("\nDetailed Metrics:")
print(f"  NDVI: {result['ndvi']:.3f} ({result['vegetation_health']})")
print(f"  NDVI Score: {result['ndvi_score']:.3f}")
print(f"  Agricultural Potential: {result['agricultural_potential']:.3f}")

if 'population_pressure' in result:
    pressure = result['population_pressure']
    print(f"\nPopulation Pressure:")
    print(f"  Pressure Index: {pressure['pressure_index']:.3f}")
    print(f"  Assessment: {pressure['assessment']}")

# Drought risk assessment
print("\nAssessing drought risk...")
drought_risk = scorer.compute_drought_risk(
    ndvi=result['ndvi'],
    ndvi_historical=0.45  # Example historical average
)

print(f"  Drought Risk Score: {drought_risk['drought_risk_score']:.3f}")
print(f"  Risk Level: {drought_risk['risk_level']}")
