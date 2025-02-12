from fastapi import FastAPI
from .routers.auth import router as auth_router
from .routers.items import router as items_router
from .database import init_db, close_db

app = FastAPI(title="FastAPI MongoDB JWT")

# Register routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(items_router, prefix="/items", tags=["items"])

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.on_event("shutdown")
async def shutdown_event():
    await close_db()

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI MongoDB JWT API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)