"""
Example: Basic usage of devscore package
"""

from devscore import compute_development_score

# Example coordinates (Nairobi, Kenya)
lat = -1.2921
lon = 36.8219

print("Computing development score for Nairobi, Kenya...")
print(f"Coordinates: ({lat}, {lon})\n")

# Compute development score
result = compute_development_score(lat, lon, buffer_km=5, year=2023)

# Access results
print(f"\nOverall Development Score: {result['overall']:.3f}")
print(f"Classification: {result['classification']}")

print("\nComponent Scores:")
for component, score in result['components'].items():
    print(f"  {component}: {score:.3f}")
