import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from app.models import TaskResponse

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """You are a task triage assistant. Analyze the task and return ONLY a JSON object with these exact fields:
- priority: "low", "medium", or "high"
- category: "bug", "feature", or "support"
- estimated_effort: like "2 hours"
- suggested_team: like "backend"
- reasoning: one sentence

Return ONLY valid JSON. No other text."""


def triage_task(description: str) -> TaskResponse:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"{SYSTEM_PROMPT}\n\nTask: {description}",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_json_schema=TaskResponse.model_json_schema(),
        ),
    )

    data = json.loads(response.text)
    return TaskResponse(**data)