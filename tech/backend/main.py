from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import SensorData, AutomationData
from database import get_db_connection
from mqtt_client import start_mqtt_client
import uvicorn

app = FastAPI()

# Configuração do CORS
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    start_mqtt_client()

@app.get("/sensor", response_model=list[SensorData])
async def get_sensor_data():
    conn = get_db_connection()
    cursor = conn.execute('SELECT created_at, value FROM sensor')
    rows = cursor.fetchall()
    conn.close()
    return [{"created_at": row[0], "value": row[1]} for row in rows]

@app.get("/automation/latest", response_model=AutomationData)
async def get_latest_automation_data():
    conn = get_db_connection()
    cursor = conn.execute('SELECT created_at, state FROM automation ORDER BY created_at DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"created_at": row[0], "state": row[1]}
    else:
        raise HTTPException(status_code=404, detail="No automation data found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
