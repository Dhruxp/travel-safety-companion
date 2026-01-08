from fastapi import APIRouter, HTTPException
from backend.schemas import RouteRequest
from risk_engine.api_adapter import run_risk_engine

router = APIRouter()

@router.post("/evaluate-route")
def evaluate_route(request: RouteRequest):
    try:
        payload = request.dict()
        result = run_risk_engine(payload)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
