import uvicorn

if __name__ == "__main__":
    uvicorn.run("api.server:app", reload=True)
