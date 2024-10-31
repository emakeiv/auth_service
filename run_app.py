import uvicorn

def start_api():
      uvicorn.run("src.api.server:app", host="0.0.0.0", port=8080, reload=True)

if __name__ == "__main__":
    start_api()