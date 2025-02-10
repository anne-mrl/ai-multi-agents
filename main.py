import subprocess
import threading
import uvicorn
from app.api import app


if __name__ == "__main__":

    # Start Streamlit in separated thread to not block FastAPI
    def run_streamlit():
        subprocess.run(["streamlit", "run", "app/view.py", "--server.port=8501"])
    thread = threading.Thread(target=run_streamlit, daemon=True).start()

    # Start FastAPI server
    uvicorn.run(app, host="0.0.0.0", port=5000)
