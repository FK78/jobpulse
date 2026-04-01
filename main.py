from fastapi import FastAPI

app = FastAPI(title="Job Pulse", version="0.1.0")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}