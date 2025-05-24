import threading
import time
from bot import check_and_generate
from dashboard import app

def run_bot():
    while True:
        check_and_generate()
        time.sleep(15)

def run_dashboard():
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    threading.Thread(target=run_dashboard).start()