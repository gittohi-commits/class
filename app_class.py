from fastapi_offline import FastAPIOffline

app = FastAPIOffline()

@app.get("/")
def say_hello():
    return {"hello" : "world"}
