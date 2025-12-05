"""
Example: Compare multiple locations
"""

from devscore.scoring.final_score import DevelopmentScoreCalculator

# Initialize calculator
calculator = DevelopmentScoreCalculator()

# Define locations to compare
locations = [
    (-1.2921, 36.8219),   # Nairobi, Kenya
    (6.5244, 3.3792),     # Lagos, Nigeria
    (-26.2041, 28.0473),  # Johannesburg, South Africa
]

location_names = ["Nairobi", "Lagos", "Johannesburg"]

print("Comparing development scores across African cities...\n")

# Compute scores
results = []
for (lat, lon), name in zip(locations, location_names):
    print(f"\nProcessing {name}...")
    score = calculator.compute_development_score(lat, lon)
    results.append({
        'name': name,
        'score': score['overall'],
        'components': score['components']
    })

# Display comparison
print("\n" + "="*70)
print("COMPARISON RESULTS")
print("="*70)

# Sort by score
results.sort(key=lambda x: x['score'], reverse=True)

for i, result in enumerate(results, 1):
    print(f"\n{i}. {result['name']}")
    print(f"   Overall Score: {result['score']:.3f}")
    print(f"   Components:")
    for comp, val in result['components'].items():
        print(f"     - {comp}: {val:.3f}")
