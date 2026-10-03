from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routers.courses import router as courses_router
from app.api.v1.routers.announcements import router as announcements_router
from app.api.v1.routers.gallery import router as gallery_router
from app.api.v1.routers.testimonials import router as testimonials_router
from app.api.v1.routers.students import router as students_router
from app.api.v1.routers.demo_bookings import (
    router as demo_bookings_router,
)
from app.api.v1.routers.course_materials import (
    router as course_materials_router,
)
from app.api.v1.routers.contact import router as contact_router

app = FastAPI(
    title="Reboot Code Academy API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    courses_router,
    prefix="/api/v1",
)

app.include_router(
    contact_router,
    prefix="/api/v1",
)

app.include_router(
    announcements_router,
    prefix="/api/v1",
)

app.include_router(
    gallery_router,
    prefix="/api/v1",
)

app.include_router(
    testimonials_router,
    prefix="/api/v1",
)

app.include_router(
    students_router,
    prefix="/api/v1",
)

app.include_router(
    demo_bookings_router,
    prefix="/api/v1",
)

app.include_router(
    course_materials_router,
    prefix="/api/v1",
)

app.include_router(
    courses_router,
    prefix="/api/v1",
)

@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "Reboot Code Academy API is running",
    }