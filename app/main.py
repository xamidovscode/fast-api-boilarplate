from fastapi import FastAPI

app = FastAPI(
    title='HR SELLER APP',
    description='Seller app for IMB HR',
)


@app.get("/")
async def root():
    return {"message": "Hello World"}