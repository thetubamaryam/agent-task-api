import uuid
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from app.agent import triage_task
from app.auth import verify_api_key
from app.models import TaskRequest, TaskResponse
from app.logging_config import setup_logging

load_dotenv()
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="Task Triage Agent")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/task", response_model=TaskResponse)
def process_task(
    request: TaskRequest,
    api_key: str = Depends(verify_api_key),
):
    request_id = str(uuid.uuid4())
    logger.info(f"task_received id={request_id}")

    try:
        result = triage_task(request.description)
        logger.info(f"task_completed id={request_id}")
        return result
    except Exception as e:
        logger.error(f"task_failed id={request_id} error={e}")
        raise HTTPException(status_code=500, detail="Agent failed")