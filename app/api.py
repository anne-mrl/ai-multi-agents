from fastapi import FastAPI, HTTPException
from typing import Dict, List
from agents.agent_factory import AgentFactory
from database.sqlite3_database import SQLite3Database


app = FastAPI(title="AI Assistant",
              description="Welcome to multi-agent AI Assistant app"
              )

# Init Main Agent
r2d2 = AgentFactory.create_main_agent()


@app.get("/ask/")
async def ask(question: str) -> Dict[str, str]:
    """Endpoint to ask question to Agent A."""
    try:
        response = r2d2.process_request(question)
        # Save request in db
        SQLite3Database().save_request(question, response)
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"response": response}


@app.get("/history/")
async def history() -> Dict[str, List[Dict[str, str]]]:
    """Endpoint to get requests history."""
    try:
        history_data = SQLite3Database().get_history()
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"history": [{"question": q, "response": r, "timestamp": t} for q, r, t in history_data]}
