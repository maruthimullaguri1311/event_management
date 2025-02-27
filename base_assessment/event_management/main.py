from fastapi import FastAPI
from database import init_db
from endpoints.events import router as events_router
from endpoints.attendees import router as attendees_router
from endpoints.auth_endpoints import router as auth_router
from attendee_csv import router as csv_router
init_db()


app = FastAPI()


app.include_router(events_router, prefix="/api")
app.include_router(attendees_router, prefix="/api")
app.include_router(auth_router, prefix="/auth")
app.include_router(csv_router,prefix='/csv')
@app.get("/")
def read_root():
    return {"message": "Event Management API"}