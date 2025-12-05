"""
Example: Working with component scores
"""

from devscore.data import (
    get_satellite_features,
    get_nightlights,
    get_infrastructure_data,
    get_population_density
)

from devscore.scoring import (
    compute_poverty_score,
    compute_market_access_score,
    compute_infrastructure_score
)

# Location: Kigali, Rwanda
lat, lon = -1.9536, 30.0606

print("Collecting data for Kigali, Rwanda...")
print("="*60)

# Collect individual data sources
satellite = get_satellite_features(lat, lon)
print(f"\nSatellite - NDVI: {satellite['ndvi']:.3f}")
print(f"Vegetation Health: {satellite['vegetation_health']}")

nightlights = get_nightlights(lat, lon)
print(f"\nNightlights Intensity: {nightlights['intensity']:.2f}")
print(f"Classification: {nightlights['classification']}")

infrastructure = get_infrastructure_data(lat, lon)
amenities = infrastructure['amenity_counts']
print(f"\nInfrastructure:")
print(f"  Schools: {amenities['schools']}")
print(f"  Health facilities: {amenities['health']}")
print(f"  Markets: {amenities['markets']}")
print(f"  Banks: {amenities['banks']}")

population = get_population_density(lat, lon)
print(f"\nPopulation Density: {population['population_density']:.0f} per km²")

# Compute component scores
print("\n" + "="*60)
print("Component Scores:")
print("="*60)

all_data = {
    'satellite': satellite,
    'nightlights': nightlights,
    'infrastructure': infrastructure,
    'population': population
}

poverty = compute_poverty_score(all_data)
print(f"\nPoverty Score: {poverty['poverty_score']:.3f}")
print(f"Classification: {poverty['classification']}")

market_access = compute_market_access_score(lat, lon, infrastructure, population)
print(f"\nMarket Access Score: {market_access['score']:.3f}")
print(f"Classification: {market_access['classification']}")

infra_score = compute_infrastructure_score(infrastructure, population)
print(f"\nInfrastructure Score: {infra_score['overall_score']:.3f}")
print(f"Classification: {infra_score['classification']}")
