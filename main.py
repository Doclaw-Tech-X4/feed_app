import uvicorn

def main() -> None:
    print("Hello from feed-app!")

if __name__ == "__main__":
    uvicorn.run("app.feed_app.app:app", host="0.0.0.0", port=8000, reload=True)