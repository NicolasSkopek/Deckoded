import threading
from fastapi import FastAPI
import uvicorn

app = FastAPI()

game_instance = None

@app.get("/score")
def get_points():
    global game_instance
    if game_instance:
        return {"score": game_instance.score}
    return {"score": 0}

@app.get("/")
def get_run():
    return {"message": "Game is running"}

def start_api(game=None):
    global game_instance
    if game:
        game_instance = game
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()

def start_api_thread(game=None):
    thread = threading.Thread(target=start_api, args=(game,), daemon=True)
    thread.start()

def set_game_instance(game):
    global game_instance
    game_instance = game