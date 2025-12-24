import osmnx as ox
from risk_engine.graphs import load_graph
from risk_engine.routes import generate_routes
#feat:
from risk_engine.features import (
    lighting_score,
    isolation_score,
    crime_density,
    emergency_access_score,
    traffic_score
)
#score:
from risk_engine.scoring import (
    weights,
    score_route,
    normalise_features,
)
#explain:
from risk_engine.explainibility import explain_features
FEATURE_RANGE = {
    "crime": (0.0, 0.02),
    "isolation": (0.0, 200.0),
    "traffic": (0.0, 1.0),
}
def extract_features(route_gdf, crime_gdf=None, context= "night"):
    features= {}
    if context in ["night", "women"]:
        features["isolation"] = isolation_score(route_gdf)
        features["lighting"] = lighting_score(route_gdf)
        if crime_gdf is not None:
            features["crime"] = crime_density(route_gdf, crime_gdf)
        else:
            features["crime"] = 0.0
    if context == "ambulance":
        features["emergency"] = emergency_access_score(route_gdf)
        features["traffic"] = traffic_score(route_gdf)
    return features
def evaluate_routes(
        place: str,
        origin: tuple,
        destination: tuple,
        context: str="night",
        crime_gdf=None,
        k :int=3
):
    if context not in weights:
        raise ValueError(f"Unknown context '{context}'")
    G = load_graph(place)
    routes = generate_routes(G, origin, destination, k)
    results = []
    for idx, route in enumerate(routes):
        route_gdf = ox.routing.route_to_gdf(G, route)
        if crime_gdf is not None:
            crime_gdf = crime_gdf.to_crs(epsg = 3857)
        raw_features = extract_features(route_gdf, crime_gdf, context)
        features = normalise_features(raw_features, FEATURE_RANGE)
        risk_score = score_route(features, weights[context])
        explanation = explain_features(features, context)
        results.append({
            "route_index": idx,
            "risk_score": risk_score,
            "features": features,
            "explanation": explanation,
            "route_gdf": route_gdf
        })
    results.sort(key=lambda x: x["risk_score"])
    return results
# some bs
"""results = evaluate_routes(
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
    print("-" * 40)"""

