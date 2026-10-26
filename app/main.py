from fastapi import FastAPI

app = FastAPI(title="E-commerce Backend")


@app.get("/")
def health_check():
    return {"status": "ok", "message": "E-commerce API is running"}