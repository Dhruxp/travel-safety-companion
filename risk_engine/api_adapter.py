from typing import Dict, Any, List
from risk_engine.pipeline.route_risk_pipeline import evaluate_routes
def run_risk_engine(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Expected json format:
    {
        "place": "City, Country",
        "origin": [lat, lon],
        "destination": [lat, lon],
        "context": "night" | "women" | "ambulance",
        "k": 3
    }
    """
    if "place" not in payload:
        raise ValueError("Missing required field: place")
    if "origin" not in payload or "destination" not in payload:
        raise ValueError("Missing required field: origin or destination")
    place: str = payload["place"]
    origin: tuple = tuple(payload["origin"])
    destination: tuple = tuple(payload["destination"])
    context: str = payload.get("context", "night")
    k: int = payload.get("k", 3)
    results = evaluate_routes(
        place=place,
        origin=origin,
        destination=destination,
        context=context,
        k=k,
        crime_gdf=None   # real crime data we can use later
    )
    response = {
        "context": context,
        "best_route": {
            "risk_score": results[0]["risk_score"],
            "explanation": results[0]["explanation"]
        },
        "alternatives": [
            {
                "risk_score": r["risk_score"],
                "explanation": r["explanation"]
            }
            for r in results[1:]
        ]
    }

    return response
# Avanish, this is mainly for your techstack to follow