from fastapi import FastAPI, File, UploadFile
import pandas as pd
import os


app = FastAPI()

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_FOLDER}/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename, "message": "File uploaded successfully"}

@app.get("/data/{file_name}")
async def get_csv_data(file_name: str):
    file_path = f"{UPLOAD_FOLDER}/{file_name}"
    if not os.path.exists(file_path):
        return {"error": "File not found"}
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

