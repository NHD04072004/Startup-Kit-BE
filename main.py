from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.auth.router import router as auth_router
from src.users.router import router as users_router
from src.database.core import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Startup Investment Platform API",
    description="API for connecting startups and investors.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Startup Investment Platform API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)