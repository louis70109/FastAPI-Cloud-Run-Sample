from fastapi import FastAPI
import json, os

if os.getenv('API_ENV') != 'production':
    from dotenv import load_dotenv

    load_dotenv()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get('PORT', default=8000))
    debug = True if os.environ.get(
        'API_ENV', default='develop') == 'develop' else False
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
