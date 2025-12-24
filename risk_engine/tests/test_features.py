from pipeline.route_risk_pipeline import extract_features, evaluate_routes
results = evaluate_routes(
    place="Bengaluru, India",
    origin=(12.9716, 77.5946),
    destination=(12.9784, 77.6408),
    context="night",
    k=3,
    crime_gdf=None  # plug real data later
)

for r in results:
    print("Score:", r["risk_score"])
    print("Why:", r["explanation"])
    print("-" * 40)
