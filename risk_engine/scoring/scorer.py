def score_route(features: dict, weights: dict) -> float:
    risk_score = 0.0 # lower is better
    for feature_name, weight in weights.items():
        if feature_name not in features:
            raise KeyError(f'Feature {feature_name} missing in features dictionary')
        feature_value = features[feature_name]
        if not (0.0 <= feature_value <= 1.0):
            raise ValueError(f'Feature value for {feature_name} must be between 0 and 1')
        risk_score += feature_value * weight
    return risk_score
#Integration test
"""features = {
    "lighting": 0.8,
    "isolation": 0.2,
    "crime": 0.1
}

weights = {
    "lighting": -0.6,
    "isolation": 0.4,
    "crime": 0.5
}

b = score_route(features, weights)
print(b)  """ 
# Expected output: negative 

