from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello Minh user v2",
        "version": "2"
        }
