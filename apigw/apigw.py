from fastapi import FastAPI
import httpx

app = FastAPI()

# Endpoint en Servicio Orquetador para iniciar la orquestación
@app.get("/orquestar")
async def orquestar():
    async with httpx.AsyncClient() as client:
        try:
            respuesta_a = await client.get("http://serviciolenin:8000/serviciolenin")
            data_a = respuesta_a.json()
        except httpx.RequestError:
            data_a = "El servicio de Lenin no está disponible"

    return {"respuesta Lenin": data_a}