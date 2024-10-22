from fastapi import FastAPI

app = FastAPI()

@app.get("/serviciolenin")
async def root():
    return {"message": "Lenin was here"}
