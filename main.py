from fastapi import FastAPI
import pandas as pd
import os 

app = FastAPI()

@app.get("/vsechno")
async def vsechno():
    if os.path.exists("akris.csv"):
        try:
            df = pd.read_csv("akris.csv", error_bad_lines=False)
            return df.to_dict(orient="records")
        except pd.errors.ParserError:
            return {"error": "Error parsing akris.csv"}
    else:
        return {"error": "File akris.csv does not exist"}