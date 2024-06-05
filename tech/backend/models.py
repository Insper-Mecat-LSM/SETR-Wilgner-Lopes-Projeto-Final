from pydantic import BaseModel
from datetime import datetime

class SensorData(BaseModel):
    created_at: datetime
    value: float

class AutomationData(BaseModel):
    created_at: datetime
    state: str