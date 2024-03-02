from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
from typing import List
import pandas as pd
from app import detect_anomalies


app = FastAPI()


class ColumnData(BaseModel):
    values: List[float]
    timestamps: List[int]

class AnomalyDetectionInput(BaseModel):
    speed: ColumnData
    distance: ColumnData
    step_count: ColumnData


@app.post("/detect_anomalies/")
async def detect(input: AnomalyDetectionInput):
    try:
        # Convert the input data into pandas DataFrames
        speed_df = pd.DataFrame({
            'speed': input.speed.values,
            'timestamp': input.speed.timestamps
        })
        
        distance_df = pd.DataFrame({
            'distance': input.distance.values,
            'timestamp': input.distance.timestamps
        })
        
        step_count_df = pd.DataFrame({
            'step_count': input.step_count.values,
            'timestamp': input.step_count.timestamps
        })
        
        # Call the detect_anomalies function with the DataFrames
        result = detect_anomalies(speed_df, distance_df, step_count_df)
        
        # Return the result
        return {"anomalies_detected": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
