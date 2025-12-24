#currently all my scores are normalised between 0 and 1 but not always
#should only be used when upscaled
def min_max_normaliser(value, min_value, max_value):
    if max_value - min_value == 0:
        return 0.0
    return (value - min_value) / (max_value - min_value)
def clamp(value, min_value=0.0, max_value=1.0):
    return max(min_value, min(value, max_value))
def normalise_features(features: dict, feature_ranges: dict) -> dict:
    normalised = {}
    for feature, value in features.items():
        if feature in feature_ranges:
            min_v, max_v = feature_ranges[feature]
            normalised_value = min_max_normaliser(value, min_v, max_v)
            normalised[feature] = clamp(normalised_value)
        else:
            normalised[feature] = clamp(value)
    return normalised
