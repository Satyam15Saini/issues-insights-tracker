from fastapi import FastAPI
from routes import issues
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(issues.router)

# Optional CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"msg": "Issues & Insights Tracker is running"}
