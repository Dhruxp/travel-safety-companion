from risk_engine.pipeline.route_risk_pipeline import evaluate_routes
PLACE = "Bengaluru, India"
ORIGIN = (12.9716, 77.5946)       # MG Road
DESTINATION = (12.9784, 77.6408)  # Indiranagar

CONTEXT = "ambulance"  # we can try for others also
print("Running route safety demo...\n")
results = evaluate_routes(
    place=PLACE,
    origin=ORIGIN,
    destination=DESTINATION,
    context=CONTEXT,
    k=3,
    crime_gdf=None  # plug real crime data later
)
for idx, result in enumerate(results):
    print(f"Route Rank #{idx + 1}")
    print(f"Risk Score: {result['risk_score']:.3f}")
    print("Reasons:")
    for reason in result["explanation"]:
        print(" -", reason)
    print("-" * 50)
