from pydantic import BaseModel
from typing import List, Optional

class RouteRequest(BaseModel):
    place: str
    origin: List[float]        # [lat, lon]
    destination: List[float]
    context: Optional[str] = "night"
    k: Optional[int] = 3
