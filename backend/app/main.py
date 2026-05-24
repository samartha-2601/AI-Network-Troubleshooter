from fastapi import FastAPI

app = FastAPI(
    title="AI Network Troubleshooter",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "AI Network Troubleshooter API Running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }