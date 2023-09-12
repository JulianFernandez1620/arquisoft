from fastapi import FastAPI
from routes.message import route

app = FastAPI(
    title="Messages Microservice",
    description="Microservice in charge of air traffic controller messages"
)
app.include_router(route)



