def explain_features(features: dict, context: str) -> list:
    explainations = []
    lighting = features.get("lighting")
    isolation = features.get("isolation")
    crime = features.get("crime")
    emergency = features.get("emergency")
    if context in ["night","women"]:
        if lighting is not None:
            if lighting < 0.4:
                explainations.append("The route has poor lighting, which may increase safety risks.")
            elif lighting > 0.7:
                explainations.append("The route is well-lit, enhancing visibility and safety.")
        if isolation is not None:
            if isolation > 0.6:
                explainations.append("The route is quite isolated, which may pose safety concerns.")
            elif isolation < 0.3:
                explainations.append("The route is in a populated area, which can enhance safety.")
        if crime is not None:
            if crime > 0.5:
                explainations.append("The area has a high crime rate, which may affect safety.")
            elif crime < 0.2:
                explainations.append("The area has a low crime rate, contributing to a safer route.")
    if context == "ambulance":
        if emergency is not None:
            if emergency < 0.4:
                explainations.append("The route has low emergency service accessibility, which may delay response times.")
            elif emergency > 0.7:
                explainations.append("The route has good emergency service accessibility, ensuring quick response times.")
    if not explainations:
        explainations.append("The route features are within normal ranges, indicating a standard safety profile.")
    return explainations

# Integration test
"""features = {
    "lighting": 0.3,
    "isolation": 0.7,
    "crime": 0.6
}
b = explain_features(features, context="night")
print(b)"""
# Expected output: List of explanations regarding poor lighting, high isolation, and high crime rate

            