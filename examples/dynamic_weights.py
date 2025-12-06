"""
Example: Using dynamic weighting methods for development score calculation.
Demonstrates how to use different weighting methods instead of fixed weights.
"""

import numpy as np
import pandas as pd
from devscore.scoring.final_score import DevelopmentScoreCalculator
from devscore.scoring.weights import (
    WeightCalculator, 
    AHPWeightCalculator,
    determine_optimal_weights
)


def example_1_ahp_weights():
    """
    Example 1: Using AHP (Analytical Hierarchy Process) weights.
    Based on expert judgment and research consensus.
    """
    print("=" * 70)
    print("Example 1: AHP-based Weights (Expert Judgment)")
    print("=" * 70)
    
    # Create calculator with AHP method (default)
    calculator = DevelopmentScoreCalculator(weight_method='ahp')
    
    print("\nAHP Weights:")
    for component, weight in calculator.weights.items():
        print(f"  {component:20s}: {weight:.3f}")
    
    # Calculate score for Nairobi, Kenya
    lat, lon = -1.2921, 36.8219
    result = calculator.compute_development_score(lat, lon, buffer_km=5)
    
    print(f"\nOverall Score: {result['overall_score']:.3f}")
    print(f"Classification: {result['classification'].upper()}")


def example_2_dynamic_weights_from_data():
    """
    Example 2: Calculate weights from historical data using entropy method.
    Higher entropy = more variation = more discriminating power.
    """
    print("\n" + "=" * 70)
    print("Example 2: Dynamic Weights from Data (Entropy Method)")
    print("=" * 70)
    
    # Simulate historical component scores from multiple locations
    np.random.seed(42)
    n_locations = 50
    
    historical_data = {
        'poverty': np.random.beta(2, 5, n_locations),  # Skewed distribution
        'market_access': np.random.beta(3, 3, n_locations),  # More balanced
        'infrastructure': np.random.beta(4, 3, n_locations),
        'food_security': np.random.uniform(0.3, 0.8, n_locations),  # Uniform
        'mobile_money': np.random.beta(5, 2, n_locations)  # Right-skewed
    }
    
    # Calculate weights using entropy method
    weights_entropy = determine_optimal_weights(historical_data, method='entropy')
    
    print("\nEntropy-based Weights (higher variation = higher weight):")
    for component, weight in weights_entropy.items():
        print(f"  {component:20s}: {weight:.3f}")
    
    # Use these weights in calculator
    calculator = DevelopmentScoreCalculator(custom_weights=weights_entropy)
    
    lat, lon = -1.2921, 36.8219
    result = calculator.compute_development_score(lat, lon, buffer_km=5)
    
    print(f"\nOverall Score: {result['overall_score']:.3f}")


def example_3_compare_methods():
    """
    Example 3: Compare multiple weighting methods.
    """
    print("\n" + "=" * 70)
    print("Example 3: Comparing Different Weighting Methods")
    print("=" * 70)
    
    # Simulate historical data
    np.random.seed(42)
    n_locations = 100
    
    historical_data = pd.DataFrame({
        'poverty': np.random.beta(2, 5, n_locations),
        'market_access': np.random.beta(3, 3, n_locations),
        'infrastructure': np.random.beta(4, 3, n_locations),
        'food_security': np.random.uniform(0.3, 0.8, n_locations),
        'mobile_money': np.random.beta(5, 2, n_locations)
    })
    
    # Calculate weights using different methods
    calculator = WeightCalculator()
    methods = ['equal', 'entropy', 'pca', 'cv', 'critic']
    
    print("\nComparison of Weighting Methods:")
    print("-" * 70)
    print(f"{'Method':<15} {'Poverty':<12} {'Market':<12} {'Infra':<12} {'Food':<12} {'Mobile':<12}")
    print("-" * 70)
    
    for method in methods:
        weights = calculator.calculate_weights(historical_data, method=method)
        print(f"{method:<15} ", end="")
        for comp in ['poverty', 'market_access', 'infrastructure', 'food_security', 'mobile_money']:
            print(f"{weights[comp]:<12.3f} ", end="")
        print()
    
    # AHP method
    ahp_calc = AHPWeightCalculator()
    ahp_weights = ahp_calc.get_development_weights_ahp()
    print(f"{'ahp':<15} ", end="")
    for comp in ['poverty', 'market_access', 'infrastructure', 'food_security', 'mobile_money']:
        print(f"{ahp_weights[comp]:<12.3f} ", end="")
    print()
    
    print("-" * 70)
    
    # Robust average of multiple methods
    robust_weights = calculator.calculate_robust_weights(
        historical_data, 
        methods=['entropy', 'pca', 'critic']
    )
    print(f"\n{'Robust (avg)':<15} ", end="")
    for comp in ['poverty', 'market_access', 'infrastructure', 'food_security', 'mobile_money']:
        print(f"{robust_weights[comp]:<12.3f} ", end="")
    print()


def example_4_custom_ahp_matrix():
    """
    Example 4: Using custom AHP comparison matrix.
    You can define your own expert judgments.
    """
    print("\n" + "=" * 70)
    print("Example 4: Custom AHP Matrix (User-defined Priorities)")
    print("=" * 70)
    
    # Custom comparison matrix
    # Order: poverty, market_access, infrastructure, food_security, mobile_money
    # Scale: 1=equal, 3=moderate, 5=strong, 7=very strong, 9=extreme importance
    
    # Scenario: Food security is most important (food crisis region)
    custom_matrix = np.array([
        [1,   2,   2,   1/2, 3],  # poverty
        [1/2, 1,   1,   1/3, 2],  # market_access
        [1/2, 1,   1,   1/3, 2],  # infrastructure
        [2,   3,   3,   1,   4],  # food_security (most important)
        [1/3, 1/2, 1/2, 1/4, 1],  # mobile_money
    ])
    
    ahp_calc = AHPWeightCalculator()
    weights, consistency_ratio = ahp_calc.calculate_weights_from_matrix(custom_matrix)
    
    components = ['poverty', 'market_access', 'infrastructure', 'food_security', 'mobile_money']
    weights_dict = {comp: w for comp, w in zip(components, weights)}
    
    print("\nCustom AHP Weights (Food Security Priority):")
    for component, weight in weights_dict.items():
        print(f"  {component:20s}: {weight:.3f}")
    
    print(f"\nConsistency Ratio: {consistency_ratio:.3f}")
    if consistency_ratio < 0.1:
        print("✓ Matrix is consistent (CR < 0.1)")
    else:
        print("⚠ Matrix may be inconsistent (CR >= 0.1)")
    
    # Use these weights
    calculator = DevelopmentScoreCalculator(custom_weights=weights_dict)
    
    lat, lon = -1.2921, 36.8219
    result = calculator.compute_development_score(lat, lon, buffer_km=5)
    
    print(f"\nOverall Score: {result['overall_score']:.3f}")


def example_5_update_weights_dynamically():
    """
    Example 5: Start with one method, then update weights as more data is collected.
    """
    print("\n" + "=" * 70)
    print("Example 5: Dynamic Weight Updates with New Data")
    print("=" * 70)
    
    # Start with entropy method (but no data yet, so falls back to AHP)
    calculator = DevelopmentScoreCalculator(weight_method='entropy')
    
    print("\nInitial weights (using AHP fallback):")
    if calculator.weights:
        for comp, weight in calculator.weights.items():
            print(f"  {comp:20s}: {weight:.3f}")
    
    # Simulate collecting data from multiple locations over time
    print("\n--- Collecting data from 20 locations... ---")
    
    np.random.seed(42)
    n_locations = 20
    
    historical_scores = {
        'poverty': list(np.random.beta(2, 5, n_locations)),
        'market_access': list(np.random.beta(3, 3, n_locations)),
        'infrastructure': list(np.random.beta(4, 3, n_locations)),
        'food_security': list(np.random.uniform(0.3, 0.8, n_locations)),
        'mobile_money': list(np.random.beta(5, 2, n_locations))
    }
    
    # Update weights based on collected data
    calculator.update_weights_from_data(historical_scores)
    
    print("\nUpdated weights reflect actual data patterns!")


if __name__ == "__main__":
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 10 + "DYNAMIC WEIGHTING METHODS FOR DEVSCORE" + " " * 20 + "║")
    print("╚" + "═" * 68 + "╝")
    
    # Run examples
    example_1_ahp_weights()
    example_2_dynamic_weights_from_data()
    example_3_compare_methods()
    example_4_custom_ahp_matrix()
    example_5_update_weights_dynamically()
    
    print("\n" + "=" * 70)
    print("Summary of Weighting Methods:")
    print("=" * 70)
    print("""
1. FIXED: Traditional fixed weights (0.35, 0.20, 0.20, 0.15, 0.10)
   → Use when: Following established research conventions

2. AHP: Analytical Hierarchy Process (expert-based)
   → Use when: Expert knowledge available, limited data
   → Default method for single locations

3. ENTROPY: Information theory-based (data variation)
   → Use when: Have historical data, want objective weights
   → Higher variation = higher weight

4. PCA: Principal Component Analysis (variance explained)
   → Use when: Have correlated indicators, want dimensionality reduction
   
5. CRITIC: Combines std + correlation structure
   → Use when: Want both variation AND uniqueness of information
   
6. CV: Coefficient of Variation (discriminating power)
   → Use when: Want simple variability-based weights

7. AUTO: Robust average of entropy, PCA, and CRITIC
   → Use when: Want balanced, data-driven weights
   → Recommended for production use with sufficient data

Recommendation: Use 'auto' with 50+ locations for robust results.
""")
    print("=" * 70)
